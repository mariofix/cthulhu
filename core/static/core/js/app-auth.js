var config = window.config = {},
$ref = $("#ref");
function animate(e) {
  var o = "animated " + e.name;
  $(e.selector).addClass(o).one("webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend",
  function() {
    $(this).removeClass(o)
  })
}
config.ResponsiveBootstrapToolkitVisibilityDivs = {
  xs: $('<div class="device-xs \t\t\t\t  hidden-sm-up"></div>'),
  sm: $('<div class="device-sm hidden-xs-down hidden-md-up"></div>'),
  md: $('<div class="device-md hidden-sm-down hidden-lg-up"></div>'),
  lg: $('<div class="device-lg hidden-md-down hidden-xl-up"></div>'),
  xl: $('<div class="device-xl hidden-lg-down\t\t\t  "></div>')
},
ResponsiveBootstrapToolkit.use("Custom", config.ResponsiveBootstrapToolkitVisibilityDivs),
config.validations = {
  debug: !0,
  errorClass: "has-error",
  validClass: "success",
  errorElement: "span",
  highlight: function(e, o, t) {
    $(e).parents("div.form-group").addClass(o).removeClass(t)
  },
  unhighlight: function(e, o, t) {
    $(e).parents(".has-error").removeClass(o).addClass(t)
  },
  submitHandler: function(e) {
    e.submit()
  }
},
config.delayTime = 50,
config.chart = {},
config.chart.colorPrimary = tinycolor($ref.find(".chart .color-primary").css("color")),
config.chart.colorSecondary = tinycolor($ref.find(".chart .color-secondary").css("color")),
$(function() {
  var t = $(".item-actions-dropdown");
  $(document).on("click",
  function(e) {
    $(e.target).closest(".item-actions-dropdown").length || t.removeClass("active")
  }),
  $(".item-actions-toggle-btn").on("click",
  function(e) {
    e.preventDefault();
    var o = $(this).closest(".item-actions-dropdown");
    t.not(o).removeClass("active"),
    o.toggleClass("active")
  })
});
var npSettings = {
  easing: "ease",
  speed: 500
};
function setSameHeights(e) {
  e = e || $(".sameheight-container");
  var t = ResponsiveBootstrapToolkit.current();
  e.each(function() {
    var e = $(this).find(".sameheight-item"),
    o = 0;
    e.each(function() {
      $(this).css({
        height: "auto"
      }),
      o = Math.max(o, $(this).innerHeight())
    }),
    e.each(function() { - 1 === ($(this).data("exclude") || "").split(",").indexOf(t) && $(this).innerHeight(o)
    })
  })
}
NProgress.configure(npSettings),
$(function() {
  var e;
  setSameHeights(),
  $(window).resize(function() {
    clearTimeout(e),
    e = setTimeout(setSameHeights, 150)
  })
}),
$(function() {
  animate({
    name: "flipInY",
    selector: ".error-card > .error-title-block"
  }),
  setTimeout(function() {
    var e = $(".error-card > .error-container");
    animate({
      name: "fadeInUp",
      selector: e
    }),
    e.addClass("visible")
  },
  1e3)
}),
$(function() {
  if (!$("#login-form").length) return ! 1;
  var e = {
    rules: {
      username: {
        required: !0,
        email: !0
      },
      password: "required",
      agree: "required"
    },
    messages: {
      username: {
        required: "Please enter username",
        email: "Please enter a valid email address"
      },
      password: "Please enter password",
      agree: "Please accept our policy"
    },
    invalidHandler: function() {
      animate({
        name: "shake",
        selector: ".auth-container > .card"
      })
    }
  };
  $.extend(e, config.validations),
  $("#login-form").validate(e)
}),
$(function() {
  if (!$("#reset-form").length) return ! 1;
  var e = {
    rules: {
      email1: {
        required: !0,
        email: !0
      }
    },
    messages: {
      email1: {
        required: "Please enter email address",
        email: "Please enter a valid email address"
      }
    },
    invalidHandler: function() {
      animate({
        name: "shake",
        selector: ".auth-container > .card"
      })
    }
  };
  $.extend(e, config.validations),
  $("#reset-form").validate(e)
}),
$(function() {
  if (!$("#signup-form").length) return ! 1;
  var e = {
    rules: {
      firstname: {
        required: !0
      },
      lastname: {
        required: !0
      },
      email: {
        required: !0,
        email: !0
      },
      password: {
        required: !0,
        minlength: 8
      },
      retype_password: {
        required: !0,
        minlength: 8,
        equalTo: "#password"
      },
      agree: {
        required: !0
      }
    },
    groups: {
      name: "firstname lastname",
      pass: "password retype_password"
    },
    errorPlacement: function(e, o) {
      "firstname" == o.attr("name") || "lastname" == o.attr("name") ? (e.insertAfter($("#lastname").closest(".row")), o.parents("div.form-group").addClass("has-error")) : "password" == o.attr("name") || "retype_password" == o.attr("name") ? (e.insertAfter($("#retype_password").closest(".row")), o.parents("div.form-group").addClass("has-error")) : "agree" == o.attr("name") ? e.insertAfter("#agree-text") : e.insertAfter(o)
    },
    messages: {
      firstname: "Please enter firstname and lastname",
      lastname: "Please enter firstname and lastname",
      email: {
        required: "Please enter email",
        email: "Please enter a valid email address"
      },
      password: {
        required: "Please enter password fields.",
        minlength: "Passwords should be at least 8 characters."
      },
      retype_password: {
        required: "Please enter password fields.",
        minlength: "Passwords should be at least 8 characters."
      },
      agree: "Please accept our policy"
    },
    invalidHandler: function() {
      animate({
        name: "shake",
        selector: ".auth-container > .card"
      })
    }
  };
  $.extend(e, config.validations),
  $("#signup-form").validate(e)
}),

$(function() {
  $(".actions-list > li").on("click", ".check",
  function(e) {
    e.preventDefault(),
    $(this).parents(".tasks-item").find(".checkbox").prop("checked", !0),
    removeActionList()
  })
}),
$(function() {
  if (!$(".form-control").length) return ! 1;
  $(".form-control").focus(function() {
    $(this).siblings(".input-group-addon").addClass("focus")
  }),
  $(".form-control").blur(function() {
    $(this).siblings(".input-group-addon").removeClass("focus")
  })
});

$(function() {
  var e, t = ((e = localStorage.getItem("themeSettings") ? JSON.parse(localStorage.getItem("themeSettings")) : {}).headerPosition = e.headerPosition || "", e.sidebarPosition = e.sidebarPosition || "", e.footerPosition = e.footerPosition || "", e),
  o = $("#app"),
  r = $("#theme-style"),
  a = $("#customize-menu"),
  i = a.find(".color-item"),
  n = a.find(".radio");
  function s() { (function() {
      t.themeName ? r.attr("href", "css/app-" + t.themeName + ".css") : r.attr("href", "css/app.css");
      return o.removeClass("header-fixed footer-fixed sidebar-fixed"),
      o.addClass(t.headerPosition),
      o.addClass(t.footerPosition),
      o.addClass(t.sidebarPosition),
      o
    })().delay(config.delayTime).queue(function(e) {
      config.chart.colorPrimary = tinycolor($ref.find(".chart .color-primary").css("color")),
      config.chart.colorSecondary = tinycolor($ref.find(".chart .color-secondary").css("color")),
      i.each(function() {
        $(this).data("theme") === t.themeName ? $(this).addClass("active") : $(this).removeClass("active")
      }),
      n.each(function() {
        var e = $(this).prop("name"),
        o = $(this).val();
        t[e] === o ? $(this).prop("checked", !0) : $(this).prop("checked", !1)
      }),
      localStorage.setItem("themeSettings", JSON.stringify(t)),
      $(document).trigger("themechange"),
      e()
    })
  }
  s(),
  i.on("click",
  function() {
    t.themeName = $(this).data("theme"),
    s()
  }),
  n.on("click",
  function() {
    var e = $(this).prop("name"),
    o = $(this).val();
    t[e] = o,
    s()
  })
}),
$(function() {
  $("body").addClass("loaded")
}),
NProgress.start(),
NProgress.done();