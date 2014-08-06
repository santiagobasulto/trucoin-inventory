'use strict';

/**
 * @ngdoc service
 * @name inventoryAppApp.MultiProductLoader
 * @description
 * # MultiProductLoader
 * Factory in the inventoryAppApp.
 */
angular.module('inventoryAppApp')
  .factory('MultiProductLoader', ['Product', '$q', function(Product, $q){
    return function(){
      var delay = $q.defer();
      Product.query(function(products) {
        delay.resolve(products['objects']);
      }, function() {
        delay.reject('Unable to fetch products');
      });
      return delay.promise;
    }
  }]);
