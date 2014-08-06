'use strict';

describe('Controller: MainCtrl', function () {

  // load the controller's module
  beforeEach(module('inventoryAppApp'));

  var MainCtrl,
    product,
    mockBackend,
    $scope;

  beforeEach(inject(function($rootScope, $controller, _$httpBackend_, Product) {
    product = Product;
    mockBackend = _$httpBackend_;
    $scope = $rootScope.$new();
    MainCtrl = $controller('MainCtrl', {
      $scope: $scope,
      products: [1, 2, 3]
    });
  }));

  it('should have list of products', function() {
    expect($scope.products).toEqual([1, 2, 3]);
  });
});
