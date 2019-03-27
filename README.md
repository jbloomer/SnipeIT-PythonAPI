# SnipeIT Python API
Use this package to interface with the SnipeIT (https://snipeitapp.com/) API directly from Python.

## Installation
Run the command `pip install snipeit`

## Usage
  * See Example Scripts included in package for specific calls

## API Features
  - [X] Hardware
  - [X] Companies
  - [X] Locations
  - [X] Accessories
  - [X] Consumables
  - [X] Components
  - [X] Users
  - [X] Status Labels
  - [X] Models
  - [X] Licenses
  - [X] Categories
  - [X] Manufacturers
  - [X] Custom Fieldsets
  - [X] Maintenances

  ![Completed](http://progressed.io/bar/100?title=completed)
  <!-- Progress is calculated by (100/14)*<Number of Checked Boxes> -->

## Release History
* 0.11
  * Completing API features based on Snipe-IT version 4.6.14
    * Added Categories class
	* Added Fieldsets class
	* Added Missing Licenses class
	* Added Manufacturers class
	* Added Maintenances class
	* Added docstrings for each methods
	* Removed unrelated methods in some classes
	* Added search() method for all supported APIs
	* Update get() methods to incorporate ordering
    * Added many new methods in each class (see documentation files)
	* Added documentation files     
* 0.10
  * Update import issue in python3
    * Updated __init__.py to python 3 import style
* 0.9
  * Created Support for Models
    * Added get() method to get JSON dump of Models
    * Added create() method to add new items to Models
    * Added getID() method to get the ID of a specified Models
    * Added delete() method to remove items from Models
    * Added updateModel() method (Uses PATCH call) to update details on a existing Model

* 0.8
  * Created Support for StatusLabels
    * Added get() method to get JSON dump of Status Labels
    * Added create() method to add new items to Status Labels
    * Added getID() method to get the ID of a specified Status Labels
    * Added delete() method to remove items from Status Labels
    * Added updateStatusLabels() method (Uses PATCH call) to update details on a existing Status Label

* 0.7
  * Created Support for Users
    * Added get() method to get JSON dump of Users
    * Added create() method to add new items to Users
    * Added getID() method to get the ID of a specified Users
    * Added delete() method to remove items from Users
    * Added updateUser() method (Uses PATCH call) to update details on a existing Users
    * Added getCheckedOutAssets() method to get a list of Assets assigned to that User

* 0.6
  * Created Support for Components
    * Added get() method to get JSON dump of Components
    * Added create() method to add new items to Components
    * Added getID() method to get the ID of a specified Components
    * Added viewID() method to see details of Components

* 0.5
  * Creating Support for Consumable API Calls
    * Added get() method to get JSON dump of Consumables
    * Added create() method to add new items to Consumables
    * Added getID() method to get the ID of a specified consumable
    * Added viewID() method to get details of a specific consumable

* 0.4
  * Creating Support for Accessory API Calls
    * Added get() method to get JSON dump of AccessoriesID
    * Added create() method to add new items to Accessories
    * Added getID() method to get the ID of a specified accessories
    * Added viewID() method to get details of a specific accessory

* 0.3
  * Creating Support for Locations API Calls
    * Added get() method to get JSON dump of locations
    * Added create() method to add new items to locations
    * Added getID() method to get the ID of a specified locations
    * Added updateCompany() method (Uses PATCH call) to update the name of an existing location.
    * Added delete() method to remove items from locations

* 0.2
  * Creating Support for Company API Calls
    * Added get() method to get JSON dump of companies
    * Added create() method to add new items to companies
    * Added getID() method to get the ID of a specified company
    * Added delete() method to remove items from companies
    * Added updateCompany() method (Uses PATCH call) to update the name of an existing company.

* 0.1
  * Created Support for Assets
      * Added get() method to get JSON dump of inventory
      * Added create() method to add new items to inventory
      * Added getID() method to get the ID of a specified device in the inventory
      * Added delete() method to remove items from inventory
      * Added updateDevice() method (Uses PATCH call) to update details on a device currently in inventory.

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits
Cox Automotive Inc.
  * https://www.coxautoinc.com/
  * Author: Jared Bloomer

## License
This Project is currently released under the MIT license. For the latest copy of the MIT license please refer to https://opensource.org/licenses/MIT
