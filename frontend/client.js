if (Meteor.isClient) {
  // counter starts at 0
  Session.setDefault('counter', 0);

  Template.hello.helpers({
    counter: function () {
      return Session.get('counter');
    }
  });

  Template.routeSearch.events({
    "submit .routeSearchForm": function (event) {
      // Prevent default browser form submit
      event.preventDefault();
      console.log("submitting!")

      // Get value from form element
      var from = event.target.fromInput.value;
      var to = event.target.toInput.value;

      // Insert a task into the collection
      Session.set('from', from);
      Session.set('to', to);
      // Clear form
      event.target.textevent.target.fromInput.value = "";
      event.target.textevent.target.toInput.value = "";
    }
  });

  Template.routeSearch.helpers({
    from: function(){
      return Session.get('from')
    },
    to: function(){
      return Session.get('to')

    }
  })
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
