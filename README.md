
# <h1 align="center">Generative-AI-tattoo-recommender-system</h1>

## <h3 align="center">The aim is to provide personalized Tattoo recommendations based on painting titles to prevent decision paralysis.</h3>
---
### <h3 align="left">Inspiration</h3>
---
By providing personalized recommendations based on analysis of user reviews of top Canadian beers, the system can help users discover new and interesting beers from Canada that they might not have otherwise considered. At the same time, by identifying common words and themes in the reviews, the system can provide valuable insights into the factors that are most important to users when choosing a Canadian beer. These insights could be used by Canadian breweries and other stakeholders in the beer industry to better understand and meet the needs and preferences of their customers, which in turn could lead to more informed product development and marketing efforts specifically targeting the Canadian market.

### <h3 align="left">How does it work</h3>
---
This system is a responsive web application built using Flask. Its interface is designed using HTML and CSS from scratch. The user can input their favorite beer and receive recommendations for similar beers based on the singular value decomposition (SVD) and cosine similarity model. The Natural Language Toolkit (NLTK) is also used to identify the most common words in user comments. When a user inputs a beer through the interface, a function in the Flask app is called to process the data and display the predicted outcomes.

### <h3 align="left">Tools and Libraries used</h3>
---

* openai API
* Pandas
* streamlit


### <h3 align="left">Dataset</h3>
---
For this project I scrapped data from [BeerAdvocate](https://www.beeradvocate.com) which is then stored in beer_final1.csv. This CSV file 
contains:

* 8 columns (Beer_name, User, Rating, Comment, %, City, Country, Image)
* 450 unique beers
* 14688 rows

### <h3 align="left">Project Demo</h3>
---
![Demo GIF](https://github.com/Virat199608/Beer-Reccomendation-system/blob/master/beerdemo1.gif)

