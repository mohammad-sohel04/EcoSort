# EcoSort

EcoSort is an intelligent waste segregation system designed to efficiently differentiate between biodegradable and non-biodegradable waste using advanced machine learning (ML) algorithms and image processing techniques. This project aims to enhance the recycling process and promote sustainable waste management practices.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Project Overview

EcoSort leverages the power of machine learning and image processing to automate the waste segregation process, increasing efficiency by 85%(***update this***). The system is deployed on a Raspberry Pi, enabling real-time processing and decision-making.

## Features

- **Intelligent Waste Segregation:** Utilizes ML algorithms to classify waste.
- **Image Processing:** Processes images to identify and categorize waste items.
- **Real-Time Processing:** Deployed on a Raspberry Pi for immediate action and response.
- **Increased Efficiency:** Improves waste segregation accuracy by 85%, reducing the need for manual 

***addition of application data***

## Technologies Used

- **Machine Learning:** Developed using Python and popular ML libraries such as TensorFlow and Scikit-learn. ****we didnt use it**
- **Image Processing:** Implemented with OpenCV.
- **Hardware:** Raspberry Pi for real-time processing and deployment.
- **Other Tools:** NumPy, Pandas for data handling, and Jupyter Notebooks for experimentation and prototyping.

# Dataset
Annotted dataset is divided into 3 parts
1. Training set
2. Validation set
3. Test set


## Setup
Create a virtual envirnment
```bash
python -m venv venv
```

activate the virtual envirnment
```bash
.\venv\Scripts\Activate.ps1 
```

## Usage

To use EcoSort, follow these steps:
1. You can use an Aurdiono based Setup to classify the input images for classifcation and sorting

    1. Connect your camera and sensors to the Raspberry Pi.
    2. Run the main script to start the waste segregation process:
    ```bash
    python run.py
    ```

    3. The system will process the waste items in real-time and segregate them accordingly.

2. Use the mobile application provided to run the garabge classification model
    
    ****need to be updated***

3. Use windows for system system deployment
    ```bash
    garbagesort.exe
    ```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## Contact
If you have any questions or need further information, feel free to contact us though issues section:
