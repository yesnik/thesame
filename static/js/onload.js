$(document).ready(function(){

	$('a[data-rel]').each(function() {
		$(this).attr('rel', $(this).data('rel'));
	});

	$('.up').click(function(){
		$('html, body').animate({scrollTop:0}, 800);
		return false;
	});

	/**
	* BEGIN StyleSheetSwitcher
	**/
	var $sheets = $('#stylesheet_switcher #stylesheets');
	$('#stylesheet_switcher #switcher').click(function(){
		if( $(this).hasClass('active') ) {
			$(this).removeClass('active');
			$sheets.removeClass('active');
		}
		else {
			$(this).addClass('active');
			$sheets.addClass('active');
		}
	});
	
	$.stylesheetInit();
	$('#stylesheet_switcher #stylesheets li a').bind(
		'click',
		function(e)
		{
			$('#stylesheet_switcher #stylesheets li a').removeClass('active');
			$(this).addClass('active');
			$.stylesheetSwitch(this.getAttribute('id'));
			return false;
		}
	);
	/**
	* END StyleSheetSwitcher
	**/
	
	});
	
	$(window).load(function(){
	
	/**
	* BEGIN Plugins
	**/
	$('.accordion').accordion({collapsible: true});
	$('.clearinput').clearInputValue();
	$('.flexslider').flexslider();
	$('.lightbox').prettyPhoto({social_tools: '', theme: 'pp_default'});
	$('.tabs').tabs();
	/**
	* END Plugins
	**/
	
	/**
	* BEGIN Internet Explorer Hacks
	**/
	$('.breadcrumbs a:last-child').addClass('last-child');
	$('table tbody tr:nth-child(2n+1)').addClass('odd');
	$('table tbody tr:nth-child(2n)').addClass('even');
	/**
	* END Internet Explorer Hacks
	**/
	
	/**
	* BEGIN Ajax Form
	**/
	
	$('#ajaxform').submit(function(event){
		event.preventDefault();
		
		
		var $form = $( this )
		var name = $form.find( 'input[name="form_name"]' )
		var email = $form.find( 'input[name="form_email"]' )
		var subject = $form.find( 'input[name="form_subject"]' )
		var message = $form.find( 'textarea[name="form_comment"]' )
	
		var verification=true;
	
		if(name.val()==''){
			verification=false;
		}
	
		if(email.val()==''){
			verification=false;
		}
	
		if(subject.val()==''){
			verification=false;
		}
	
		if(message.val()==''){
			verification=false;
		}
	
		if(verification==true){
			$('#result').fadeIn();
			$('#result').html('<em>Please Wait...</em>');
	
			$.ajax({
				type: 'POST',
				url: 'php/email_send.php',
				data: $(this).serialize()
			})
			.done(
				function( msg ) {
					if(msg=='1'){
						$('#result').fadeOut();
						$('#result').html('<div class="success">Message has been sent</div>');
						$('#result').prettyPhoto({
							social_tools: '',
							theme: 'ajaxform'
						});
						$.prettyPhoto.open('#result');
	
						name.val('');
						email.val('');
						subject.val('');
						message.val('');
						$.prettyPhoto.open('#result');
					}
					else{
						$('#result').html('<em>Form is not sent. Error.</em>');
					}
					$('#result').delay(3000).fadeOut();
				}
		   );
	   }
	   else{
			$('#result').html('<em>Some fields are empty.</em>');
	   }
	   
	});
	/**
	* END Form Ajax
	**/
	
	
	$('#top_menu li').each(function(index, el){
		if($(el).find('div.submenu').length > 0){
			$(el).hover(
				function(){ $(this).find('div.submenu').css('display', 'block'); },
				function(){ $(this).find('div.submenu').css('display', 'none'); }
			);
		}
	});
	
	$('.page_gallery .image').each(function(index, el){
		$(el).hover(
			function(){ $(this).find('.caption').css('display', 'block'); },
			function(){ $(this).find('.caption').css('display', 'none'); }
		);
	});

	var $filterType = $('#portfolio_categories li.active a').attr('class');
	var $holder = $('.portfolio_items');
	var $data = $holder.clone();
	jQuery('#portfolio_categories li a').click(function(e) {
		$('#portfolio_categories li').removeClass('active');
		var $filterType = $(this).attr('class');
		$(this).parent().addClass('active');
	
		if ($filterType == 'all') {
			var $filteredData = $data.find('li');
		}
		else {
			var $filteredData = $data.find('li[data-type=' + $filterType + ']');
		}
		$holder.quicksand(
			$filteredData,
			function()
			{
				$('.lightbox').prettyPhoto({social_tools: ''});
			}
		);
		return false;
	});


});

(function($){
    $.fn.extend({
        clearInputValue: function(){
            return this.each(function() {
                var obj = $(this);
				var text = obj.val();

				obj.focus(function(){
					if(obj.val() == text) obj.val('');
				});

				obj.blur(function(){
					if(obj.val() == '') obj.val(text);
				});
            });
        }
    });
})(jQuery);