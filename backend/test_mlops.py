from app.mlops.monitoring_manager import (
    EnterpriseMonitoringManager,
)

result = (

    EnterpriseMonitoringManager

    .monitor_prediction(

        model_name="BankruptcyModel",

        prediction="Low Risk",

        probabilities=[0.08, 0.92],

        features={

            "debt_ratio": 0.32,

            "current_ratio": 2.1,

        },

    )

)

print(result)

dashboard = (

    EnterpriseMonitoringManager

    .dashboard()

)

print(dashboard)