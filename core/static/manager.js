var app = angular.module('APP', []);
app.controller('invoice', ['$scope', '$http', function($scope, $http) {
	$http({
		url: '',
		method: 'POST'
	})
	.then((res)=>{
		$scope.invoices = res.data;
	}, (err)=>{
		console.error(err);
	})
}]);