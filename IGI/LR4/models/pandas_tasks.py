"""
Module: pandas_tasks
Task B: Pandas — Stroke Prediction Dataset
Variant 19:
  Part A: Series from avg_glucose_level, add median as new element
  Part B: Ratio of avg glucose: stroke == 1 vs stroke == 0
"""

import pandas as pd
import numpy as np


def create_sample_stroke_data():
    return pd.DataFrame({
        'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'gender': ['Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
        'age': [67, 61, 80, 49, 79, 81, 78, 35, 54, 44],
        'hypertension': [0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        'heart_disease': [1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        'ever_married': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes'],
        'work_type': ['Private', 'Self-employed', 'Private', 'Private', 'Private', 'Self-employed', 'Private', 'Govt_job', 'Private', 'Private'],
        'Residence_type': ['Urban', 'Rural', 'Urban', 'Urban', 'Rural', 'Urban', 'Rural', 'Urban', 'Urban', 'Rural'],
        'avg_glucose_level': [228.69, 88.91, 82.50, 77.91, 150.24, 93.24, 97.63, 67.10, 82.60, 110.25],
        'bmi': [36.6, 29.7, 34.4, 28.9, 32.8, 36.6, 29.4, 23.7, 27.4, 26.7],
        'smoking_status': ['never smoked', 'formerly smoked', 'formerly smoked', 'never smoked', 'never smoked', 'formerly smoked', 'never smoked', 'never smoked', 'formerly smoked', 'never smoked'],
        'stroke': [1, 0, 0, 1, 1, 1, 1, 0, 0, 0]
    })


def load_stroke_data():
    """
    Load real stroke prediction dataset if available, otherwise use sample.
    """
    try:
        # Try to read real CSV from data folder
        df = pd.read_csv('data/stroke_data.csv')
        print("Loaded real stroke dataset from data/stroke_data.csv")
        return df
    except FileNotFoundError:
        print("Real dataset not found. Using sample data.")
        return create_sample_stroke_data()


def main_pandas_cli():
    print("\n=== Task B: Pandas — Stroke Prediction Dataset (Variant 19) ===")

    # Load dataset
    df = load_stroke_data()
    print("\nDataset info:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    
    print("\nFirst 5 rows:")
    print(df.head())
    
    # ========== PART A: Series from avg_glucose_level ==========
    print("\n" + "="*50)
    print("PART A: Series from avg_glucose_level")
    print("="*50)
    
    # 1. Create Series from avg_glucose_level column
    avg_glucose_series = df['avg_glucose_level'].copy()
    avg_glucose_series.name = 'avg_glucose_level'
    
    print("\nOriginal Series (first 10):")
    print(avg_glucose_series.head(10))
    
    # 2. Calculate median
    median_value = avg_glucose_series.median()
    print(f"\nMedian of avg_glucose_level: {median_value:.2f}")
    
    # 3. Add median as new element with index 'median'
    # Using pd.concat to add a new element
    median_series = pd.Series([median_value], index=['median'], name='avg_glucose_level')
    avg_glucose_with_median = pd.concat([avg_glucose_series, median_series])
    
    print("\nSeries with median added (last element):")
    print(avg_glucose_with_median.tail())
    
    # ========== PART B: Statistical ratio ==========
    print("\n" + "="*50)
    print("PART B: Statistical calculation")
    print("="*50)
    
    # Separate patients with and without stroke
    stroke_patients = df[df['stroke'] == 1]
    no_stroke_patients = df[df['stroke'] == 0]
    
    print(f"\nPatients with stroke (stroke == 1): {len(stroke_patients)}")
    print(f"Patients without stroke (stroke == 0): {len(no_stroke_patients)}")
    
    # Calculate mean glucose level
    mean_glucose_stroke = stroke_patients['avg_glucose_level'].mean()
    mean_glucose_no_stroke = no_stroke_patients['avg_glucose_level'].mean()
    
    print(f"\nAverage glucose level (stroke patients): {mean_glucose_stroke:.2f}")
    print(f"Average glucose level (non-stroke patients): {mean_glucose_no_stroke:.2f}")
    
    # Calculate ratio (how many times higher)
    if mean_glucose_no_stroke != 0:
        ratio = mean_glucose_stroke / mean_glucose_no_stroke
        print(f"\nRatio (stroke / non-stroke): {ratio:.2f}")
        print(f"Interpretation: Glucose level in stroke patients is {ratio:.2f} times higher than in non-stroke patients.")
    else:
        print("\nCannot calculate ratio: mean glucose in non-stroke is zero.")
    
    # Additional statistics for better understanding
    print("\n" + "="*50)
    print("Additional statistics:")
    print("="*50)
    print(f"Median glucose (stroke): {stroke_patients['avg_glucose_level'].median():.2f}")
    print(f"Median glucose (non-stroke): {no_stroke_patients['avg_glucose_level'].median():.2f}")
    print(f"Std glucose (stroke): {stroke_patients['avg_glucose_level'].std():.2f}")
    print(f"Std glucose (non-stroke): {no_stroke_patients['avg_glucose_level'].std():.2f}")
    
    # Show individual values for clarity
    print("\nIndividual glucose levels:")
    print("\nStroke patients (stroke == 1):")
    for idx, row in stroke_patients.iterrows():
        print(f"  Patient {int(row['id'])}: {row['avg_glucose_level']:.2f}")
    
    print("\nNon-stroke patients (stroke == 0):")
    for idx, row in no_stroke_patients.iterrows():
        print(f"  Patient {int(row['id'])}: {row['avg_glucose_level']:.2f}")


if __name__ == "__main__":
    main_pandas_cli()