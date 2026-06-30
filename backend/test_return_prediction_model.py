import numpy as np

from app.risk.models.return_prediction_model import (
    ReturnPredictionModel,
)

###########################################################

X_train = np.random.rand(

    100,

    12,

)

y_train = np.random.uniform(

    -20,

    40,

    100,

)

###########################################################

model = ReturnPredictionModel()

model.fit(

    X_train,

    y_train,

)

###########################################################

prediction = model.predict(

    X_train[:5]

)

###########################################################

print()

print("=" * 60)

print("RETURN PREDICTION MODEL")

print("=" * 60)

print()

print(

    prediction

)

###########################################################

model.save()

print()

print(

    "Model saved successfully."

)