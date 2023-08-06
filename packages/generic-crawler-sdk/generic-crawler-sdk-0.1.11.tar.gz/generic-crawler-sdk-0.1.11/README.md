# Introduction
Generic Crawler SDK is a web crawling framework used to extract structured data from world wide web. It can be used for a wide range of purposes, from data mining for intelligent analytics to monitoring competitor pricing.

![](docs/images/generic-crawler-logomsu.png)

## Architecture
Generic Crawler SDK is designed as client-server model that connects executed defined crawler actions from client-side with REST Api to handling all incoming requests and returning extracted data from crawler engine.

![](docs/architecture/generic-crawler-arch-fordocs.png)

## Requirements
* Works on Linux, Windows. Simply any environment, where Python can be installed is suitable to install this SDK. 
* Python minimum versin of 3.8 should be installed. Official address to download is [https://www.python.org/downloads/](https://www.python.org/downloads/).
* SDK communincates with the crawler service. Therefore applying whitelisting for the network is required: 
    * service endpoint URL 
    * outbound port 443(https)

## Installation

### Installing via pip 
Since the SDK is a pip package, it can be easily installed via pip. Creating a virtual environment is recommended.

![](docs/images/install.png)

### Setting up user specific variables
Once the package is installed .env file needs to be configured, in order to provide access token and endpoint url to the SDK. Create ".env" file in the root directory and add user specific variables as below:

![](docs/images/docs/images/dotenv-file.png)

# Usage 

## Config

Config is an object. Its main function is to load user-specific variables from dotenv file and provide those to other objects, such as GenericCrawler. Currently there is two user-specific variables, which are service enpoint url and access token.

![](docs/images/docs/images/docs/images/config-object.png)

## Action Reader
ActionReader is an object. Its main function is to read, load Action files and validates for structural correctness of the format. In a case where user has written an action which includes an unimplemented attribute or missing one, it will throw Exception.

![](docs/images/actionreader-schema-validation.png)

ActionReader object has one attribute: **action**. Loaded valid action file is converted into Dict and assigned to this attribute.

![](docs/images/actionreader-reader-action.png)



## Generic Crawler
The main function of GenericCrawler object is to send requests to remote crawler service with payload including actions loaded by ActionReader. During instantiation GenericCrawler object checks the health status of remote endpoint of crawler service. If only service is up and ready, object is created. 

![](docs/images/genericcrawler.png)


Instantiated crawler onject has two attributes: endpoint & is_alive.

![](docs/images/genericcrawler-attributes.png)

It has single method, retrieve(). Retrieve method is called with argument of action method of ActionReader. Once it is called, the request is sent to crawler service and waited for a response.

![](docs/images/genericcrawler-retrieve.png)

Crawler service executes actions defined by the users action.yaml file and returns the extracted data from targets or exception detail if there is an error during crawling.

![](docs/images/genericcrawler-retrieve-result.png)

Retrieve method of GenericCrawler object returns parsed extracted data and response object. Response object is returned only for debugging purposes. Therefore it can be ignored. Extracted data is converted into Python Dictionary.

![](docs/images/generic-crawler-data.png)

Keys in dictionary are named based on targets of users action.yaml file.

![](docs/images/target-keyvalue-dummy.png)


Succesfully crawled data can be further processed & stored by user.

## Action Components
Actions are yaml formatted files, where browser interactions are defined and consist of two components; **steps & targets**. Action files should include name, url info:

![](docs/images/sample-action-1.png)

### Steps
Steps point to elements and describe specific actions on those, which are required in order to reach the target element(s).

#### do-nothing
Literally does nothing. Because generic crawler always requires minimum a single step to execute, use this action if there is no step required to extract the target.

![](docs/images/step-do-nothing.png)

#### wait-for 
Waits for given duration.

![](docs/images/step-wait-for.png)

#### click 
Mouse click on given element selector

![](docs/images/step-click.png)

#### write 
Write specific string on given element selector. When "wait" is true, the step waits for elements visibility & presence before executing (see step [wait](#wait)).

![](docs/images/step-write.png)

#### mouse-hover 
Move mouse (virtually) over the given selector. 

![](docs/images/step-mouse-hover.png)

#### scroll 
Scrolls page given direction; up/down. Repetition enables multiple times of scrolling for pages having infinite scroll.

![](docs/images/step-scroll.png)

#### hit-enter 
Sends keyboard event 'enter' to page.

![](docs/images/step-hit-enter.png)


#### iterate-until 
Retrieves the given parent element and starts iterating over its child elements. Iteration continues until given condition applies. The condition is a string search and its match. Once the looked up child element is found, it executes custom action (e.g.: click, write, etc).

![](docs/images/step-iterate-until.png)

#### retrieve-sitemap 
Some pages provide their entire sitemap in xml format without any GUI component. This action enables sitemap data crawling. Depth attribute defines how further crawling should progress recursively.

![](docs/images/step-retrieve-sitemap.png)

#### popup-check 
Waits for popups after page-load and dismisses if given popup window exists.

![](docs/images/step-popup-check.png)



### Targets
Targets are defined as pointers to elements using xpath/css selectors, which contain data to be extracted from pages. A crawl action can have multiple targets. Currently available target types are text, nontext, url and values of custom attributes.

#### text 
Extracts text from element, which user sees on the page.

![](docs/images/target-text.png)

#### nontext 
Extracts non-text attribute from element. Currently "image_url" is supported and available. 

![](docs/images/target-nontext.png)

#### extract-urls 
Extracts urls from href attribute of given element selector. Used with a boolean value.

![](docs/images/target-extract-urls.png)



#### attribute 
Extracts value of any given attribute from element selector. This target type returns dynamically based on value of extracted attribute. If attribute has multiple values, it returns a list of values, otherwise single string of value is retruend. 

![](docs/images/target-attribute.png)

#### anchored-iteration 
This type of target includes a parent selector and its child selector(s). Child selectors consists of Anchor and Target. Then anchor and target child selectors are retrieved as sub-selector of parent(s). Iteration occurs on anchor selector. Target values are extracted for each target element of each anchor. Given anchor action is taken as a mini-step on each iteration between anchors, so that target values are available. Values of anchors are also extracted. Finally service returns a dictionary of extracted Anchor values and Target values of each anchor belonging to parent selector.

![](docs/images/target-anchored-iteration.png)


## Error Handling
Crawler service tries to catch as diverse error types as possible on executing crawler actions. Any error caused by missing or mismatched selector is returned to developer using SDK. Developer is expected to handle response of crawler on his/her pyhon script, whether succesfully extracted data or an error message containing exception details is returned. On unexpected, unclear error messages you can contact to "TEAM-AI@turkcell.com.tr" for further investigation. If the error is browser drvier related, the exact error detail text is reflected as it it returned from driver, (e.g: ERR_NAME_NOT_RESOLVED error caused by trying to navigate non-existing URL). 


#### Selector Error:

When given selector not found

![](docs/images/error-message-selector.png)


#### URL Error:  

When non-existing URL is tried to crawl

![](docs/images/error-message-nonexist-url.png)


### Connection Error:

Due to security concerns, Generic Crawler Service lives in an environment, where only specific page categories are whitelisted. Some pages might be grouped as malicious or dangerous in terms of Turkcell's security policies, therefore those might be excluded in the whitelist. In this regard if connection is dropped/failed by the firewall policy rules, SDK will return a connection error.

![](docs/images/error-message-connection.png)


# Use Case Examples
We provide some use case examples, which are ready-to-use. Those are heavily commented, so that reader has a comprehension on how to implement crawler bots using this crawler framework SDK. 
For each crawler use case to be implemented, with which this SDK is used, we write a python script file and action files in yml format. Action files can be as many distinct files as possible for each browser interaction required to exrtract the data. 


## Example (1) - Crawling the seller info from an ecommerce marketplace site
In this use case which we need to crawl and extract sellers information from a ecommerce marketplace site, the files are as below:

- **crawl_seller_page.py** ; crawler logic
- **actions_seller_page.yml** ; defined interactions as shown in above sections [steps & targets](#steps) described above. 

![](docs/images/example-action-seller-yaml.png)

![](docs/images/example-action-seller-py.png)

## Example (2) - Pagination of tariff details on a telecom operator site
Pagination is important aspect of data extraction from web pages. Some pages reuqiure to click "Next" button or another method to see all the list of items displayed. Here we crawl all the partially displayed tariff details from each page.

Note: \break .../li/[**last()**] target selector used below is to retrieve last item from list of pagination related elements. You can consult the official xpath documentation for the usage details of last() function: [https://developer.mozilla.org/en-US/docs/Web/XPath/Functions/last](https://developer.mozilla.org/en-US/docs/Web/XPath/Functions/last)

- **action_pagination.yml** ; defined interactions as shown in above sections [steps & targets](#steps) described above.
- **crawl_products_using_pagination.py** ; crawler logic


![](docs/images/example-action-pagination-yaml.png)

![](docs/images/example-crawl-products-using-pagination-py.png)


# Contact
We would like to hear about any feature requests, bug reports, issues, or any kind of questions regarding this crawler framework SDK and also its Documentation, which you are currently reading. Please feel free to contact us at anytime.

**TEAM-SENSAI** - [team-sensai@turkcell.entp.tgc](mailto:TEAM-SENSAI@turkcell.entp.tgc)
