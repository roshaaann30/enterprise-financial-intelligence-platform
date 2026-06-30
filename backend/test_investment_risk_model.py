from app.risk.datasets.investment_dataset import InvestmentDataset
from app.risk.preprocessing.investment_preprocessor import InvestmentPreprocessor
from app.risk.models.investment_risk_model import InvestmentRiskModel

dataset = InvestmentDataset()
data = dataset.process()

preprocessor = InvestmentPreprocessor()

processed = preprocessor.process(
    data["X"],
    data["y"],
)

model = InvestmentRiskModel()

model.fit(
    processed["X_train"],
    processed["y_train"],
)

model.save()

print("Investment Risk Model Saved Successfully")