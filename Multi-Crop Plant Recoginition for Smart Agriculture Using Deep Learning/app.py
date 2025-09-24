import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import matplotlib.cm as cm
import av
import openai

openai.api_key = "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"

av.logging.set_level(av.logging.ERROR)

# Load your trained model
model = tf.keras.models.load_model('final_trained_model.keras')

# Use the same class labels as during training
CLASS_LABELS = ['Aji pepper plant',
 'Almonds plant',
 'Amaranth plant',
 'Apples plant',
 'Artichoke plant',
 'Avocados plant',
 'Bananas plant',
 'Barley plant',
 'Beets plant',
 'Black pepper plant',
 'Blueberries plant',
 'Bok choy plant',
 'Brazil nuts plant',
 'Broccoli plant',
 'Brussels sprout plant',
 'Buckwheat plant',
 'Cabbages and other brassicas plant',
 'Camucamu plant',
 'Carrots and turnips plant',
 'Cashew nuts plant',
 'Cassava plant',
 'Cauliflower plant',
 'Celery plant',
 'Cherimoya plant',
 'Cherry plant',
 'Chestnuts plant',
 'Chickpeas plant',
 'Chili peppers and green peppers plant',
 'Cinnamon plant',
 'Cloves plant',
 'Cocoa beans plant',
 'Coconuts plant',
 'Coffee (green) plant',
 'Collards plant',
 'Cotton lint plant',
 'Cranberries plant',
 'Cucumbers and gherkins plant',
 'Dates plant',
 'Dry beans plant',
 'Dry peas plant',
 'Durian plant',
 'Eggplants (Aubergines) plant',
 'Endive plant',
 'Fava bean plant',
 'Figs plant',
 'Flax fiber and tow plant',
 'Flaxseed (Linseed) plant',
 'Fonio plant',
 'Garlic plant',
 'Ginger plant',
 'Gooseberries plant',
 'Grapes plant',
 'Groundnuts (Peanuts) plant',
 'Guarana plant',
 'Guavas plant',
 'Habanero pepper plant',
 'Hazelnuts plant',
 'Hemp plant',
 'Hen eggs (shell weight) plant',
 'Horseradish plant',
 'Jackfruit plant',
 'Jute plant',
 'Kale plant',
 'Kohlrabi plant',
 'Leeks plant',
 'Lemons and limes plant',
 'Lentils plant',
 'Lettuce and chicory plant',
 'Lima bean plant',
 'Longan plant',
 'Lupins plant',
 'Lychee plant',
 'Maize (Corn) plant',
 'Mandarins, clementines, satsumas plant',
 'Mangoes, mangosteens, guavas plant',
 'Maracuja(Passionfruit) plant',
 'Millet plant',
 'Mint plant',
 'Mung bean plant',
 'Mustard greens plant',
 'Mustard seeds plant',
 'Navy bean plant',
 'Oats plant',
 'Oil palm fruit plant',
 'Okra plant',
 'Olives plant',
 'Onions (dry) plant',
 'Oranges plant',
 'Oregano plant',
 'Papayas plant',
 'Parsley plant',
 'Peaches and nectarines plant',
 'Peas (Green) plant',
 'Persimmons plant',
 'Pine nuts plant',
 'Pineapples plant',
 'Pinto bean plant',
 'Pistachios plant',
 'Plantains plant',
 'Pomegranates plant',
 'Potatoes plant',
 'Pumpkins, squash and gourds plant',
 'Quinoa plant',
 'Radishes and similar roots plant',
 'Rambutan plant',
 'Rapeseed (Canola) plant',
 'Raspberries plant',
 'Rice (Paddy) plant',
 'Rosemary plant',
 'Rubber (natural) plant',
 'Rye plant',
 'Saffron plant',
 'Sage plant',
 'Scallions plant',
 'Sorghum plant',
 'Soursop plant',
 'Soybeans plant',
 'Spinach plant',
 'Starfruit plant',
 'Strawberries plant',
 'Sugar beet plant',
 'Sugar cane plant',
 'Sunflower seeds plant',
 'Sweet potatoes plant',
 'Swiss chard plant',
 'Tamarind plant',
 'Taro (cocoyam) plant',
 'Tea plant',
 'Teff plant',
 'Thyme plant',
 'Tomatoes plant',
 'Triticale plant',
 'Turmeric plant',
 'Turnip greens plant',
 'Vanilla beans plant',
 'Walnuts plant',
 'Watermelons plant',
 'Wheat plant',
 'Yams plant']  # Replace with your actual list of class names, e.g. ['Wheat', 'Rice', ...]

IMG_SIZE = (224, 224)

def preprocess_image(img):
    img = img.resize(IMG_SIZE)
    arr = np.array(img) / 255.0
    if arr.shape[-1] == 4:  # Handle PNG with alpha
        arr = arr[..., :3]
    arr = np.expand_dims(arr, 0)
    return arr

def get_crop_advice(crop_name):
    prompt = f"Give agronomic care tips for the crop: {crop_name}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

#
# +++ THIS IS THE NEW, CORRECTED CODE +++
#
#
# +++ THIS IS THE FINAL, CORRECTED CODE +++
#
def make_gradcam_heatmap(img_array, model, last_conv_layer_name):
    grad_model = tf.keras.models.Model(
        [model.inputs], [model.get_layer(last_conv_layer_name).output, model.output]
    )

    with tf.GradientTape() as tape:
        # grad_model returns a list of two items. The second item (preds)
        # might ALSO be a list, e.g., [<Tensor>].
        conv_outputs, preds = grad_model(img_array)

        # Get the actual prediction tensor out of the list
        # This is the key fix!
        preds_tensor = preds[0]

        # Now use the tensor for the rest of the calculations
        pred_index = np.argmax(preds_tensor)
        class_channel = preds_tensor[:, pred_index]

    grads = tape.gradient(class_channel, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    conv_outputs = conv_outputs[0]
    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()

st.title("Multi-Crop Plant Recognition System")

uploaded_file = st.file_uploader("Upload a plant image:", type=["jpg", "jpeg", "png"])
if uploaded_file:
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption='Uploaded Crop Leaf', use_container_width=True)
    arr = preprocess_image(img)
    preds = model.predict(arr)
    idx = np.argmax(preds)
    conf = preds[0, idx]
    st.success(f"Prediction: {CLASS_LABELS[idx]} ({conf*100:.2f}% confidence)")

    if st.button("Show Explainability"):
        heatmap = make_gradcam_heatmap(arr, model, last_conv_layer_name='Conv_1')
        heatmap_img = cm.jet(heatmap)[..., :3]  # Convert to RGB
        st.image(heatmap_img, caption="Grad-CAM Heatmap", use_container_width=True)
        
    if st.button("Get Agronomic Advice"):
        tips = get_crop_advice(CLASS_LABELS[idx])
        st.write(tips)