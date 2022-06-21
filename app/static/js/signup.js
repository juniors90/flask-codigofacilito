$(document).ready(function () {
  $(".ui.form").form({
    fields: {
      name: {
        identifier: 'name',
        rules: [
          {
            type   : 'empty',
            prompt : 'Please enter your name'
          },
          {
            type: "minLength[3]",
            prompt: "Your name must be at least 3 characters",
          },
        ]
      },
      email: {
        identifier: "email",
        rules: [
          {
            type: "empty",
            prompt: "Please enter your e-mail",
          },
          {
            type: "email",
            prompt: "Please enter a valid e-mail",
          },
        ],
      },
      password: {
        identifier: "password",
        rules: [
          {
            type: "empty",
            prompt: "Please enter your password",
          },
          {
            type: "length[6]",
            prompt: "Your password must be at least 6 characters",
          },
        ],
      },
    },
  });
});
