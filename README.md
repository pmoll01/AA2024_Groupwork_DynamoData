# AA2024_Groupwork_DynamoData - EV Charging Hub Analytics

## Project Overview
This project was conducted as part of the Master's program *Analytics and Applications* at the University of Cologne. The aim is to provide data-driven insights into the operation of electric vehicle (EV) charging hubs and to develop utilization forecasts. The project follows the CRISP-DM process and includes data preparation, descriptive analytics, cluster analysis, and the development of predictive models.

## Objectives
### 1. Data Preparation
- Loading and cleaning datasets.
- Handling missing and erroneous data.

### 2. Descriptive Analytics
- **Temporal Patterns**: Analyze charging behavior over the day, week, and across seasons.
- **Key Performance Indicators (KPIs)**: Define and visualize three key time-dependent KPIs.
- **Site Characteristics**: Identify differences between public and private charging stations.

### 3. Cluster Analysis
- Create clusters to identify typical charging events.
- Interpret and name the clusters.

### 4. Utilization Prediction
- Develop two models: one based on neural networks and another using an alternative method.
- Compare model performance and recommend a suitable method.
- Develop a business case based on the findings.

## Data Description
The provided data includes charging sessions at two locations (public and private). Additional weather data is also available. Details on the dataset fields are documented in the project description.

## Technologies Used
- **Programming Languages:** Python
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn, TensorFlow/Keras
- **Tools:** Jupyter Notebook, Git

## Project Structure
```
📂 project-root/
├── 📁 data/                 # Datasets
├── 📁 notebooks/            # Jupyter Notebooks for analysis and modeling
├── 📁 visualizations/       # Visualized results
├── 📁 oldTest/              # Test files
└── README.md                # Project overview
```

## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
    Use the `environment.yml` file in the project's root folder to create an Anaconda environment:
    ```bash
    conda env create --file environment.yml
    ```
    This will create an environment named _DynamoData_. You can use it to run the Jupyter Notebooks. Activate the environment with:
    ```bash
    conda activate DynamoData
    ```
    Optionally, set it as the default environment for your IDE.

## Results and Insights
The results include:
- Descriptive analyses of charging behavior.
- KPIs for monitoring charging infrastructure.
- Clusters for typical charging events.
- Predictive models for utilization.

## Authors
This project was conducted by a team of Master's students:
- Justin Reichert
- Fynn Aldenkirchs
- Timon Knüttel
- Chiara Seidenath
- Paul Moll

## Supervision
- **Supervisor:** Prof. Dr. Wolfgang Ketter
- **Tutor:** Janik Muires (muires@wiso.uni-koeln.de)
