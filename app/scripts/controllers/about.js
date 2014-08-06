'use strict';

/**
 * @ngdoc function
 * @name inventoryAppApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the inventoryAppApp
 */
angular.module('inventoryAppApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
