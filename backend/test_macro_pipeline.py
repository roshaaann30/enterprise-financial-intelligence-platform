from app.features.macro.pipeline import (
    MacroPipeline,
)

macro = MacroPipeline.process()

print(macro.tail())

print(macro.columns.tolist())