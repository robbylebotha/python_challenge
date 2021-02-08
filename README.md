# Using python for data analysis.
 
``Challenge 2: Sighthing data exploration
Now that you created a visualisation of the sighting data carry on a data exploration and then discuss any interesting characteristics that you found``

### Tasks
1) Use any statistical methods to find any interesting relationships, trends or holes in the data. 
2) Report on your method and explain what you found. Summarise the steps taken that led to your findings.

> `Blockquote` I decided to go for Gaussian Distribution

#### Tools: VS Code, Python, Panda, Numpy, matplotlib

**Goals:** 

 -  Wrangle location data
 - Use statistical methods to find trends, specifically peaks times of 
	traffic.      

**Steps:** 

 - Unzip zip file and extract ble location data
 - Read csv into script
 - Create data frame
 - Elminate records where lat& long = 0, I assume these are faulty packets.

> Run: python *.py
> Exmple Run **python sd_speed.py** to run the Speed Standard Deviation Map


