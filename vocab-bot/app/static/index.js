var app = new Vue({
	el: "#app",
	data: {
	}
})


var appFilterBar = new Vue({
  el: "#filterbar",
  data: {},
  methods: {
    updateWords: function() {
      console.log("Updating words")
      getWords()
    }
  }
})



var app2 = new Vue({
	el: "#words",
	data: {
    nColumns: 4,   // Number of words in row
		words: []
	},
  computed: {
    groupedWords: function() {
      var newArr = [];
      for (var i=0; i < this.words.length; i+=this.nColumns) {
        newArr.push(this.words.slice(i, i+this.nColumns))
      }
      return newArr
    }
  }

})


function getWords(category="TOFEL", n=20) {
  // Make a request for a user with a given ID
  axios.get('/backend/get_n_words', {
    params: {
      category: category,
      n: n
    }
  })
    .then(function (response) {
      console.log(response);
      app2.words = response.data
    })
    .catch(function (error) {
      // handle error
      console.log(error);
    })
    .then(function () {
      // always executed
    });
}


getWords()