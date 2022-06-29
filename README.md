
# Simple Recommender System


In this project, I made a Simple 
Movie Recommender System using **Cosine
Similarity**. This recommendation system 
is made based on implicit ratings. I made 
this specifically for learning about the 
recommendation system, how they works etc.

The data is collected from **Kaggle**. You have 
to download the csv named *netflix_data.csv* from
the **data** folder in this repo. 

While doing this project, I have learned so 
many things including:

- How to make a recommendation system when 
  the data has no rating column or the ratings
  are not in a desirable format.
- I learned about using the **feather** 
  file which loads much more faster 
  than a **csv** file.
- Cleaning the data according to my needs.
- Usage of **Cosine Similarity** in 
  Recommendation System etc.
  
## Deployment

After creating the movie recommendation system,
I made a **Streamlit app** and deploy that app
in **Docker** locally. 

If you have docker installed, yoou can run this 
project in your computer. Just clone this project,
navigate to the project directory and run the 
below command in your terminal.

```bash
  docker build -t <image-name> .
```
you can give the image name according to 
your choice. After that you have to run the 
below command in your terminal.

```
  docker run --name <container-name> -p 5000:8501 <image-name>
```
That's it, you can see the application running 
in your browser.


## 🔗 Contact Me

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/srang992/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/subhradeep_rang)

