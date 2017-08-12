<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.js"></script>
<script type="text/javascript">
	$(document).ready(function(){
		$('a#sign').click(function(){
			$.ajax({
				url: '/mysite/sign/',
				type: 'POST',
				data: {'csrfmiddlewaretoken': '{{ csrf_token }}'},
				dataType: 'json',
				timeout: 10000,
				success: function(result) {
					if(result.data == "post_success") {
						alert("sign success");
						window.location.reload();
					}else {
						alert("you have signed today,please come tomorrow");
					}
				}
			});
		});
	});
</script>
