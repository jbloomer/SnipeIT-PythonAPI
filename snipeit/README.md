# SnipeIT Python API
Use this package to interface with the SnipeIT (https://snipeitapp.com/) API directly from Python.

## Installation
Run the command `pip install snipeit`

## Usage
  * See Example Scripts included in package for specific calls

## Release History
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
