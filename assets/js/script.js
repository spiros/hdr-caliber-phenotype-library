$(document).ready(function(){

$(function wrapping() {
    $('.phenotype-content h3').each(function () {
        $(this).nextUntil('h3').add(this).wrapAll('<div class="tabbed " />');
        var i=0;
		$('.tabbed').each(function(){
		    i++;
		    var newID='tab'+i;
		    $(this).attr('id',newID);
		    $(this).val(i);
		});
		$('.tabbed').first().addClass('current');
		$('ul.post-toc li').first().addClass('current');
    });
    $('.phenotype-content h4').each(function () {
        $(this).nextUntil('h4').add(this).wrapAll('<div class="subtab " />');
        var i=0;
		$('.subtab').each(function(){
		    i++;
		    var newID='subtab'+i;
		    $(this).attr('id',newID);
		    $(this).val(i);
		});

    });

});




	
	$('ul.post-toc li').click(function(){
		var index = $(this).index() + 1;

		$('ul.post-toc li').removeClass('current');
		$('.tabbed').removeClass('current');

		$(this).addClass('current');
		$('#tab' + index).addClass('current');
	});

	$('ul.post-toc li a').click(function(){
		event.preventDefault();
	});

$(function(){

    var url = window.location.pathname, 
        urlRegExp = new RegExp(url.replace(/\/$/,'') + "$"); // create regexp to match current url pathname and remove trailing slash if present as it could collide with the link in navigation in case trailing slash wasn't present there
        // now grab every link from the navigation
        $('#navbar .nav a, #navbar .nav .dropdown-menu a').each(function(){
            // and test its normalized href against the url pathname regexp
            if(urlRegExp.test(this.href.replace(/\/$/,''))){
                $(this).addClass('active');
            }
        });

});

});