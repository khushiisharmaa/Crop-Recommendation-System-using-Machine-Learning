# Crop Recommendation System Using Machine Learning

## Project Overview
This project aims to assist farmers and agricultural stakeholders in selecting the most suitable crop for cultivation based on soil and environmental conditions. By leveraging machine learning, the system provides data-driven recommendations to optimize yield and sustainability.  

## Features  
- Crop Prediction: Recommends the best crop based on input parameters such as soil type, nitrogen, phosphorus, potassium levels, pH, and weather conditions.  
- **Machine Learning Model: Trained using a robust dataset to ensure accurate and reliable predictions.  
- User-Friendly Interface: Implemented using Flask, making the system accessible and easy to use.  

## Technologies Used  
- Programming Language: Python  
- Libraries:  
  - Pandas  
  - NumPy  
  - Scikit-learn  
  - Flask  
- Model: Supervised machine learning algorithms (e.g., Decision Trees, Random Forest, or similar).  

## How to Run the Project  
1. Clone the Repository:  
   ```bash  
   git clone https://github.com/khushiisharmaa/Crop-Recommendation-System-using-Machine-Learning.git  
   ```  

2. Navigate to the Directory:  
   ```bash  
   cd Crop-Recommendation-System-using-Machine-Learning  
   ```  

3. Install Dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. Run the Flask Application:  
   ```bash  
   python app.py  
   ```  

5. Access the Application:  
   Open your browser and go to `http://127.0.0.1:5000/`.  

## Dataset
The dataset includes features like soil nutrients (N, P, K), temperature, humidity, and pH values, along with the corresponding crop labels.  

- Source:https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset  
- Preprocessing: Handled missing values and normalized features for better model performance.  

## Results & Accuracy
- The system achieves high accuracy in crop prediction due to the optimized machine learning model.  
- Provides actionable insights for sustainable agriculture and resource optimization.  

## **Future Enhancements 
- Integration with IoT Sensors: Automate data collection from fields in real-time.  
- Geographic Adaptation: Extend recommendations based on location-specific datasets.  
- Mobile App Integration: Develop a mobile-friendly interface for easier accessibility.  

## Contributing  
Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request for any improvements or suggestions.  

## Acknowledgments
- Inspired by the vision of enhancing agricultural productivity through technology.  
