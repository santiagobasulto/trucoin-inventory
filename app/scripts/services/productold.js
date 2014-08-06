'use strict';

/**
 * @ngdoc service
 * @name inventoryAppApp.Product
 * @description
 * # Product
 * Factory in the inventoryAppApp.
 */
var inventoryAppFactories = angular.module('inventoryAppFactories', ['ngResource']);

inventoryAppFactories.factory('Product', ['$resource', function($resource){
  return $resource('http://localhost:8000/api/v1/product/:id', {id: '@id'});
}]);
