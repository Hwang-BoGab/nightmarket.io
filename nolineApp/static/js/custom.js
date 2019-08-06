$(document).ready(function(){

    // anmation Event 제작
    function scroll(){
        var scrollPosition = 650;
        $("body").animate({
                scrollTop: scrollPosition
        }, 1000);

    }

    //$(".hero-banner__content").animate({ opacity: 0.25, height: '' }, 5000);

    var $offset = 500;
    var $page = $('.pages');
    //var $counters = $('.counters');
    var $pageThreshold = $page.offset().top - $offset;
    var $pageExecuted = false;

    $(window).scroll(function(){
        // service-item 나타내기
        /*if(!$pageExecuted){
            if( $(this).scrollTop() > $pageThreshold ){

                current = (this).scrollTop();
                scrollPosition = 200;

                $("body").animate({
                        scrollTop: scrollPosition;
                }, 1000);
            }
        }*/

        var $post = $('#post1')
        var $postExecuted = false;
        var $postThreshold = $post.offset().top - 300;

        // service-item 나타내기
        if(!$postExecuted){   
            if( $(this).scrollTop() > $postThreshold ){
                $post.addClass('active');
                $postExecuted = true;
            }
        }

        var $post2 = $('#post2')
        var $post2Executed = false;
        var $post2Threshold = $post2.offset().top - 300;

        // service-item 나타내기
        if(!$post2Executed){   
            if( $(this).scrollTop() > $post2Threshold ){
                $post2.addClass('active');
                $post2Executed = true;
            }
        }

        
        var $post3 = $('#post3')
        var $post3Executed = false;
        var $post3Threshold = $post3.offset().top - 300;

        // service-item 나타내기
        if(!$post3Executed){   
            if( $(this).scrollTop() > $post3Threshold ){
                $post3.addClass('active');
                $post3Executed = true;
            }
        }

        
        var $post4 = $('#post4')
        var $post4Executed = false;
        var $post4Threshold = $post4.offset().top - 300;

        // service-item 나타내기
        if(!$post4Executed){   
            if( $(this).scrollTop() > $post4Threshold ){
                $post4.addClass('active');
                $post4Executed = true;
            }
        }

    });
});