# export_ease
Built upon Python modules that call JSON RESTful API to gather macroeconomic data, this package offers a streamlined interface through which you can request and subsequently analyze vast amounts of macroeconomic data from sources including UN Comtrade and the International Monetary Fund (IMF). Below is a step-by-step guide detailing effective use of this program. (This package was built to supplement a [research project](https://github.com/pcd15/Econ-Sanctions/blob/main/README.md) led by Morad Bali at Duke University's Nicholas School of the Environment. The link provided offers further resources to tidy the data that this package writes.)
## Running the Program
### Comtrade
* This part of the program utilizes the [comtradeapicall](https://pypi.org/project/comtradeapicall/) Python package to implement additional functionality.
* To query export data from Comtrade, you can use the following methods:
  * ```get_all_exports```: writes csv file containing export data for all available country pairs (i.e., exports from each reportner to all its partners)
  * ```get_total_exports```: writes csv file containing total-export (exports to world) data for all available reporters
* When you run these functions, you'll need to enter the parameters for your query in the console. The program will ask you for the input that the query requires. Once the program's finished running, it'll output the names of the files that were just created.
### IMF
* The code to get IMF data is almost identical in structure to Comtrade's. The only difference is the input required to make the query, but there's no need to worry about accidentally typing the wrong input, as the program will both prompt you for the type of input and ensure the input is valid before making the API call.
  * If you input an incorrect country name for ```get_reporter_exports```, you can check country_codes.csv to see valid country names (this file is written by the program when you run ```get_reporter_exports```).
* Functions with which to query data:
  * ```get_reporter_exports```: writes csv file containing value exports from reporter provided in console input to all its partners 
  * ```get_total_exports```: same as Comtrade's get_total_exports method
### Other Notes
* This program assumes that the source code is contained in a subdirectory within the project (e.g., ```src```) and that the files generated will be written to another subdirectory titled ```data``` (i.e., both your source code's and ```data```'s parent directory must be the root directory for your project). Be sure that your project adheres to this structure, as this package will throw errors if it can't find ```data```.
* Data is expressed in USD (Comtrade in ones, IMF in millions) and is available in both monthly and annual quantities.
* All methods defined in this package don't require any arguments, but they will prompt you for input through the console/terminal.
* Comtrade functions will retrieve data for the given year only, while IMF functions will retrieve data starting at the given year and ending with the most recently published data.
* The ```get_reporter_exports``` function for IMF has a quirk that occurs when the user requests a query for annual data starting at a year within 3 years of the current year. In this case, the function will "override" the user's indicated year and instead make the starting year 3 years less than the current year--I had to add this padding in order to work around the varying structures of the JSON file returned by the IMF API. This has no serious implications, as it still gets all the data you requested (and then some).
## Example Python Script
```
from export_ease.comtrade import Comtrade     # importing the Comtrade class
from export_ease.imf import IMF     # importing the IMF class

comtrade_obj = Comtrade()     # creating a Comtrade object so that we can use the methods of the class we imported
imf_obj = IMF()     # creating an IMF object so that we can use the methods of the class we imported

# see above documentation
comtrade_obj.get_all_exports()
comtrade_obj.get_total_exports()

imf_obj.get_reporter_exports()
imf_obj.get_total_exports()
```

The above code can also be found in the ```test``` folder in the [GitHub repository](https://github.com/pcd15/export_pkg) for this package.
