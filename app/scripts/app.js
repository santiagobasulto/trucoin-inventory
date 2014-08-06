'use strict';

/**
 * @ngdoc overview
 * @name inventoryAppApp
 * @description
 * # inventoryAppApp
 *
 * Main module of the application.
 */
angular
  .module('inventoryAppApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        resolve: {
          products: ["MultiProductLoader", function(MultiProductLoader) {
            return MultiProductLoader();
          }]
        }
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
