var config = window.config = {};

// Config reference element
var $ref = $("#ref");

function animate(options) {
	var animationName = "animated " + options.name;
	var animationEnd = "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";
	$(options.selector)
	.addClass(animationName)
	.one(animationEnd, 
		function(){
			$(this).removeClass(animationName);
		}
	);
}

// Configure responsive bootstrap toolkit
config.ResponsiveBootstrapToolkitVisibilityDivs = {
    'xs': $('<div class="device-xs 				  hidden-sm-up"></div>'),
    'sm': $('<div class="device-sm hidden-xs-down hidden-md-up"></div>'),
    'md': $('<div class="device-md hidden-sm-down hidden-lg-up"></div>'),
    'lg': $('<div class="device-lg hidden-md-down hidden-xl-up"></div>'),
    'xl': $('<div class="device-xl hidden-lg-down			  "></div>'),
};

ResponsiveBootstrapToolkit.use('Custom', config.ResponsiveBootstrapToolkitVisibilityDivs);

//validation configuration
config.validations = {
	debug: true,
	errorClass:'has-error',
	validClass:'success',
	errorElement:"span",

	// add error class
	highlight: function(element, errorClass, validClass) {
		$(element).parents("div.form-group")
		.addClass(errorClass)
		.removeClass(validClass); 
	}, 

	// add error class
	unhighlight: function(element, errorClass, validClass) {
		$(element).parents(".has-error")
		.removeClass(errorClass)
		.addClass(validClass); 
	},

	// submit handler
    submitHandler: function(form) {
        form.submit();
    }
}

//delay time configuration
config.delayTime = 50;

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
function setSameHeights($container) {
	$container = $container || $('.sameheight-container');
	var viewport = ResponsiveBootstrapToolkit.current();
	$container.each(function() {
		var $items = $(this).find(".sameheight-item");
		// Get max height of items in container
		var maxHeight = 0;
		$items.each(function() {
			$(this).css({height: 'auto'});
			maxHeight = Math.max(maxHeight, $(this).innerHeight());
		});
		// Set heights of items
		$items.each(function() {
			// Ignored viewports for item
			var excludedStr = $(this).data('exclude') || '';
			var excluded = excludedStr.split(',');
			// Set height of element if it's not excluded on 
			if (excluded.indexOf(viewport) === -1) {
				$(this).innerHeight(maxHeight);
			}
		});
	});
}
NProgress.configure(npSettings);
$(function() {
	setSameHeights();
	var resizeTimer;
	$(window).resize(function() {
		clearTimeout(resizeTimer);
        resizeTimer = setTimeout(setSameHeights, 150);
	});
});
$(function() {
	animate({
		name: 'flipInY',
		selector: '.error-card > .error-title-block'
	});
	setTimeout(function(){
		var $el = $('.error-card > .error-container');
		animate({
			name: 'fadeInUp',
			selector: $el 
		});
		$el.addClass('visible');
	}, 1000);
});
$(function() {
  $(".actions-list > li").on("click", ".check",
  function(e) {
    e.preventDefault(),
    $(this).parents(".tasks-item").find(".checkbox").prop("checked", !0),
    removeActionList()
  })
});
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
  $("body").addClass("loaded")
});
NProgress.start();
NProgress.done();