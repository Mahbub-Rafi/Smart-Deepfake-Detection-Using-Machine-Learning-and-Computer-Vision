
# Smart Deepfake Detection Using Machine Learning and Computer Vision

This is a deepfake detection project built with Python, Django, and deep-learning algorithms (Models: Xception, MobileNetV3, DenseNet121, and ResNet50). Any user can register in the website, and after login, they can upload an image to verify whether the image is real or fake. 


## Documentation

[See Full Documentation](https://github.com/user-attachments/files/17523340/Smart.Deepfake.Detection.Using.Machine.Learning.and.Computer.Vision.pdf)


## Acknowledgements

 - [Capstone Project Showcase, Summer 2023, North South University](http://ece.northsouth.edu/capstone-design/)


## Demo

![Demo Video](https://github.com/user-attachments/assets/194b6e3c-8cb1-4ecd-9c79-3a157b68e2d3)




## Poster Presentation
![Project Poster](https://github.com/user-attachments/assets/abc676fc-1f8a-4973-addc-0e40bb86d6e4)


## Motivation

Deepfakes, a mix of "deep learning" and "fake," are synthetic media that have been digitally manipulated to successfully replace one person's image with that of another. Deepfakes are the change of a person's face using deep generative methods. The use of forgeries has the power to improve people's lives by stimulating enjoyment, cultural contact, and education. On the other hand, the widespread use of deepfake technology for nefarious objectives, such as disseminating misleading information and manipulating electronic data and proof, is a major cause of worry. While the process of making false video is not new, deepfakes use advanced machine learning and artificial intelligence algorithms to change or synthesize visual and audio information that is easier to fool. There are different sorts of deepfakes; among the main types are textual deepfakes, deepfake movies, deepfake pictures, deepfake audio, real-time or live deepfakes. Up until December 2020, over 85,000 harmful deepfake videos that were made by professional producers were found. Deepfake's repercussions include misinformation and disinformation, image and trust damage, political manipulation, privacy and consent violations, ramifications for law enforcement and justice, and security and fraud difficulties. Actors like Emma Watson and Scarlett Johansson, musicians like Katy Perry, and politicians like Barack Obama and Donald Trump were the first to have their likenesses used in deep fakes without their knowledge or consent, increasing public anxiety and awareness about the potential risks of deep fake technology. The goal of this project is to halt social crime by employing deepfake photos. We are driven to work on deepfake detection to defend people's privacy, eliminate harm, defend democracy, and avoid economic risks. Our study will apply different deep learning models to spot deep-fake photos in order to stop cybercrime. We created this project in order to defend people from bogus image bullying and to preserve data. Deepfake technology has recently caused serious worries over the security and trustworthiness of data saved online.

## Installation
To install the required packages, run the following command:

```bash
make install
```
This will install the required packages specified in the requirements.txt file.


## Run 
To run the project with npm, follow the commands:

```bash
python -m venv env
cd env\scripts
activate
cd ..
pip install django
django-admin startproject name
cd name
python manage.py startapp login
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser (follow the steps)
python manage.py runserver
```

## Methodology

### Block Diagram of the System:

![Figure 1: Block Diagram](https://github.com/user-attachments/assets/8a075e6f-4346-41c8-9797-5f7814fb6de7)

Figure 1 shows the fundamental structure of this research. The structure can take in a 2D image
from a dataset that is itself divided into actual and fabricated images, allowing for further analysis
and classification.
Before beginning model building, the dataset was segmented, the images were resized to 256 x
256 pixels, and data augmentation techniques (vertical and horizontal flipping) were applied to
enhance the dataset. The system was then trained and fine-tuned to identify the difference between
authentic and fabricated content. The model is optimized with a specified optimizer, loss function,
and evaluation metrics. Metrics like accuracy, precision, recall, F1 score, ROC curve, and AUC
curve were used to assess the model's efficacy and performance. The model's loss and accuracy
showed interesting trends as a function of ambiguity or confusion. The output component of the
model determines whether a user-submitted image is authentic or fake. A block diagram shows
the decision-making process and important parts of the framework. It gives a quick overview of
the whole system.

### Architecture of the System:

![System Architecture](https://github.com/user-attachments/assets/024675fb-fd6c-44ba-812e-2270820889b8)
## Models
- VGG16
![VGG16 Block Diagram](https://github.com/user-attachments/assets/4d7bf9bf-dd77-4c04-8694-9b2a904ecd58)

- DenseNet121
![DenseNet121 Block Diagram](https://github.com/user-attachments/assets/97222687-759a-461f-8790-68fad2d6e7de)

- MobileNetV3Small
![MobileNetV3Small Block Diagram](https://github.com/user-attachments/assets/da208b85-cafc-4c9c-8f47-c3f152a425c9)

- Xception
![Xception Block Diagram](https://github.com/user-attachments/assets/d0f99a5a-22ee-445c-95bb-c96dab14a59a)

## Results
Both the VGG16 and Xception models exhibited strong performance, with accuracy rates of 99% and 96%, respectively. These models have showcased the significant advancements in deep learning systems by effectively discerning between genuine and altered photos. Furthermore, it was observed in our trials that a level of accuracy of 98% could be achieved when testing MobileNetV3. The outstanding accuracy rates exhibited by DenseNet121 highlight its potential for reliable categorization of manipulated images. In the context of our deepfake detection project, we conducted a comparative analysis of five different neural network designs. Among these structures, Xception has shown a noteworthy validation accuracy of 96%, thereby establishing itself as the most optimal choice for the deployment of deepfake identification when compared to the other four models. These models possess the capability to discern intricate details and patterns, thereby enabling the precise identification of modified photographs. Our research demonstrates the significance of the meticulous selection of deep-learning models for the purpose of classifying fraudulent images. The Xception models' exceptional performance underlines how well they are 
able to address the problems that fake photos pose across a variety of application domains. During the course of this endeavor, we have devoted considerable consideration to several aspects, including data quality, model architecture, training technique, deployment infrastructure, and continuing maintenance. These factors have been crucial in the effective development and implementation of a deepfake detection model, which is founded on the Xception architecture. This project aims to provide assistance to individuals in their daily activities while also contributing to the advancement of research by facilitating the identification of effective CNN 48 models understanding their operational principles, and assessing their reliability and validity. The provision of public access to the system can alleviate the challenges associated with counterfeit content and deceptive information for users. 

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Mahbub-Rafi/Smart-Deepfake-Detection-Using-Machine-Learning-and-Computer-Vision/blob/main/LICENSE) file for details.

## Contributing
Pull requests are welcome! If you would like to contribute to this project, please fork the repository and create a new branch for your changes. Submit a pull request when you are ready to merge your changes back into the main branch.


## References

[1]  Y. L. Lyu, Y. Xin, S. Pu, Q. Honggang and Siwei, "Celeb-DF: A Large-Scale Challenging Dataset for DeepFake Forensics," 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 3204-3213, 2020.  

[2]  M. Khan and K. N. Alam, "Detecting Deepfake Images Using Deep Learning Techniques and Explainable AI Methods," Intelligent Automation and Soft Computing, vol. 35, July 2022.  

[3]  H. S. Shad, M. Rizvee, N. Tasnim, S. M. A. Hoq and M. M. Khan, "Comparative Analysis of Deepfake Image Detection Method using Convolutional Neural Network," Computational Intelligence and Neuroscience, p. 18, 2021.  

[4]  A. R. Nießner, C. Davide, V. Luisa, R. Christian, T. Justus and Matthias, "FaceForensics++: Learning to Detect Manipulated Facial Images," 2019.  

[5]  R. T. Ortega-Garcia, Ruben-Vera-Rodriguez, F. Julian, M. Aythami and Javier, "DeepFakes and Beyond: A Survey of Face Manipulation and Fake Detection," 2020.  

[6]  N. B. Tubaro, , . D. C. Edoardo, M. Sara, B. Luca, B. Paolo and Stefano, "Video Face Manipulation Detection Through Ensemble of CNNs," 2020 25th International Conference on Pattern Recognition (ICPR), pp. 5012-5019, 2020.  

[7]  D. Afchar, V. Nozick, J. Yamagishi and A. Darius, "MesoNet: a Compact Facial Video Forgery Detection Network," 2018 IEEE International Workshop on Information Forensics and Security (WIFS), pp. 1-7, December 2018.  

[8]  D. A. Coccomini, N. Messina, C. Gennaro and F. Falchi, "Combining EfficientNet and Vision Transformers for Video Deepfake Detection," in Lecture Notes in Computer Science, Springer International Publishing, 2022, p. 219–229. 51 

[9]  T. Nguyen, C. M. Nguyen, T. Nguyen, D. Nguyen, S. Nahavandi, V. Pham and T. Huynh The, "Deep learning for deepfakes creation and detection: a survey," Computer Vision and Image Understanding, p. 1–17, 09 2019.  

[10]  A. Elhassan, M. Al-Fawa'reh, M. Jafar, M. Abebneh and S. Jafar, "DFT-MF: Enhanced deepfake detection using mouth movement and transfer learning," SoftwareX, vol. 19, p. 101115, 2022.  

[11]  K. H. Du and Xiaoyu, "Self-Supervised Deepfake Detection by Discovering Artifact Discrepancies," 2021.  

[12]  N. M. A. Saudagar and A. K. Jilani, "Detecting Fake Images on Social Media using Machine Learning," International Journal of Advanced Computer Science and Applications, vol. 10, p. 12, 2019.  

[13]  Z. Xia, T. Qiao, M. Xu, X. Wu, L. Han and Y. Chen, "Deepfake Video Detection Based on MesoNet with Preprocessing Module," Symmetry, vol. 14, p. 05, 2022.  

[14]  H. F. Shahzad, F. Rustam, E. S. Flores, J. Luís Vidal Mazón, I. de la Torre Diez and I. Ashraf, "A Review of Image Processing Techniques for Deepfakes," Sensors, vol. 22, p. 12, 2022.  

[15]  T. Sajini, "A Survey on Deepfake Detection Techniques," in International Journal of Computer Engineering in Research Trends, 2020.  

[16]  X. Li, X. Xiao, J. Li, C. Hu, J. Yao and S. Li, "Li, Xiaojun and Xiao, Xvhao and Li, Jia and Hu, Changhua and Yao, Junping and Li, Shaochen," Scientific Reports, vol. 12, p. 6092, 04 2022.  

[17]  L. Nataraj, T. Mohammed, B. Manjunath, S. Chandrasekaran, A. Flenner, M. J. Bappy and A. Roy-Chowdhuri, "Detecting GAN generated Fake Images using Co-occurrence Matrices," Electronic Imaging, vol. 2019, pp. 532-1, 19.  

[18]  Xhlulu, "140k real and fake faces," kaggle, 15 March 2023. [Online]. Available: https://www.kaggle.com/datasets/xhlulu/140k-real-and-fakefaces.52

[19]  G. Haung, Z. Liu, L. v. d. Maaten and K. Q. Weinberger, "Densely Connected Convolutional Networks.," 2016.

[20]  K. Simonyan and A. Zisserman, "Very Deep Convolutional Networks for Large-Scale Image Recognition," 2014. 

[21]  A. Howard, M. Sandler, G. Chu, L. C. Chen, B. Chen, M. Tan, W. Wang, Y. Zhu, R. Pang, V. Vasudevan, Q. v. Le and H. Adam, "Searching for MobileNetV3, 2019. 
[22]  F. Chollet, "Xception: Deep Learning with Depthwise Separable Convolutions," 2016. 

[23]  I. Düntsch and G. Gediga, "Confusion matrices and rough set data analysis," 2019. 
