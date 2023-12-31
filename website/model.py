from roboflow import Roboflow

rf = Roboflow(api_key="S0ZRXr8KslM5xZVGkV9N")
project = rf.workspace().project("nailcheck")
model = project.version(1).model

# infer on a local image
print(model.predict("your_image.jpg").json())

# infer on an image hosted elsewhere
print(model.predict("URL_OF_YOUR_IMAGE", hosted=True).json())

# save an image annotated with your predictions
model.predict("your_image.jpg").save("prediction.jpg")