
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h2 align="center">Credit Card Fraud Detection</h2>

  <p align="center">
    Detect Fraud through credit card transactions.
    <br />
    <a href="https://github.com/angelxd84130/CreditCardFraudDetection">View Demo</a>
    ·
    <a href="https://github.com/angelxd84130/CreditCardFraudDetection/issues">Report Bug</a>
    ·
    <a href="https://github.com/angelxd84130/CreditCardFraudDetection/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


By randomly selecting training and testing data in each round, to understand the impact of features on the model.   
Then use the results to judge the performance and accuracy of each model on different training sets.

Here's why:
* Test whether random selection of training and test data affects the results
* Observe different models and compare their accuracies
* Plot the results to facilitate visual observation

After experiments, it is found that the performance of linear regression and logistic regression is very stable, but SVM and decision tree are susceptible to the influence of training data.
Therefore, the following discussion will focus on logistic regression, SVM, and decision trees.



### Built With

* [kaggle](https://www.kaggle.com/)
* [scikit-learn](https://scikit-learn.org/stable/#)
* [matplotlib](https://matplotlib.org/)



<!-- GETTING STARTED -->
## Getting Started

Start with main python file.  


### Prerequisites


1. Get the dataset from kaggle website [kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud)
2. Pull the project
3. Put the dataset in the project folder   
4. Run main.py

### Nest Steps  
1. Change the number of iterations
2. Change the random variables in transaction.py
   ```sh
   x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=200)
   ```
3. Run the project and check the results again  


<!-- USAGE EXAMPLES -->
## Usage

Use the plot to check result.  
### plot results 
![supervised learning][product-screenshot] 
### accuracy
- linearRegression: 0.9987
- logisticRegression: 0.9989
- SVM: 0.9982~9.9984
- decisionTree: 0.9991~0.9992  

The results show that linear regression and logistic regression is very stable, but SVM and decision tree are susceptible to the influence of training data



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/angelxd84130/CreditCardFraudDetection/issues) for a list of proposed features (and known issues).


<!-- CONTACT -->
## Contact

Yu-Chieh Wang - [LinkedIn](https://www.linkedin.com/in/yu-chieh-wang/)  
email: angelxd84130@gmail.com


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [kaggle-Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/angelxd84130/CreditCardFraudDetection.svg?style=for-the-badge
[contributors-url]: https://github.com/angelxd84130/CreditCardFraudDetection/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/angelxd84130/CreditCardFraudDetection.svg?style=for-the-badge
[forks-url]: https://github.com/angelxd84130/CreditCardFraudDetection/network/members
[stars-shield]: https://img.shields.io/github/stars/angelxd84130/CreditCardFraudDetection.svg?style=for-the-badge
[stars-url]: https://github.com/angelxd84130/CreditCardFraudDetection/stargazers
[issues-shield]: https://img.shields.io/github/issues/angelxd84130/CreditCardFraudDetection.svg?style=for-the-badge
[issues-url]: https://github.com/angelxd84130/CreditCardFraudDetection/issues
[license-shield]: https://img.shields.io/github/license/angelxd84130/CreditCardFraudDetection.svg?style=for-the-badge
[license-url]: https://github.com/angelxd84130/CreditCardFraudDetection/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/yu-chieh-wang/
[product-screenshot]: results.png
