'use strict';

/**
 * @ngdoc function
 * @name inventoryAppApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the inventoryAppApp
 */
angular.module('inventoryAppApp')
  .controller('MainCtrl', ['$scope', 'products', function ($scope, products) {
    $scope.products = products;
  }]);
