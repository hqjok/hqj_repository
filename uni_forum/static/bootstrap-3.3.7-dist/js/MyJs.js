/*点击刷新验证码*/
$(function () {
		$('.captcha').css('cursor', 'pointer');
		$('.captcha').click(function () {
			 $.getJSON("/captcha/refresh/",
                  function(result){
             $('.captcha').attr('src', result['image_url']);
             $('#id_captcha_0').val(result['key'])
          });
		});
	})

