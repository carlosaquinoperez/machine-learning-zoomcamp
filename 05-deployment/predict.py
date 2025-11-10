import pickle

model_file = 'pipeline_v1.bin'

with open(model_file, 'rb') as f_in:
    pipeline = pickle.load(f_in)

lead = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

prediction = pipeline.predict_proba([lead])
probability_convert = prediction[0][1]

print(f"The probability of conversion for this lead is: {probability_convert:.3f}")