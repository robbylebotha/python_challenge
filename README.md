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
 - Use statistical methods to find trends or any relationships

**I attemted to the standard deviation for the speed on the devices, in the hopes that this can be read to realiase how many people/devices in this data sample where still still or walking around the vicinity or the of the BLE Proxy devices. Glancing at the produced graph, we can see that there are very few outliers.**   

**Steps:** 

 - Unzip zip file and extract ble location data
 - Read csv into script
 - Create data frame
 - Elminate records where lat& long = 0, I assume these are faulty packets.

> Run: python *.py
> Exmple Run **python sd_speed.py** to run the Speed Standard Deviation Map
> We expect to get this output:
[Sample graph output](https://github.com/robbylebotha/python_challenge/blob/main/Figure_1.png)
 


