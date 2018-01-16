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
  - [ ] Users
  - [ ] Status Labels
  - [ ] Models
  - [ ] Licenses
  - [ ] Categories
  - [ ] Manufacturers
  - [ ] Custom Fieldsets

## Release History
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
