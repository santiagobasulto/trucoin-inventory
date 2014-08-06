'use strict';

describe('Service: MultiProductLoader', function () {

  beforeEach(function() {
    this.addMatchers({
      toEqualData: function(expected) {
        return angular.equals(this.actual, expected);
      }
    });
  });

  // load the service's module
  beforeEach(module('inventoryAppApp'));

  // instantiate service
  var MultiProductLoader, product, mockBackend, loader;
  beforeEach(inject(function (_$httpBackend_, Product, _MultiProductLoader_) {
    MultiProductLoader = _MultiProductLoader_;
    product = Product;
    mockBackend = _$httpBackend_;
    loader = _MultiProductLoader_;
  }));


  it('should do something', function () {
    expect(!!MultiProductLoader).toBe(true);
  });

  it('should load list of products', function() {
    mockBackend.expectGET('http://localhost:8000/api/v1/product').respond({
      meta: {},
      objects: [{id: 1}, {id: 2}]
    });

    var products;

    var promise = loader();
    promise.then(function(rec) {
      products = rec;
    });

    expect(products).toBeUndefined();

    mockBackend.flush();

    expect(products).toEqualData([{id: 1}, {id: 2}]);
  });
});
