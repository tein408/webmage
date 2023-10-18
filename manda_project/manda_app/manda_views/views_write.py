from django.shortcuts import redirect, render
from manda_project.manda_app.models import UserProfile

# 글쓰기
def write(request):
    if request.user.is_authenticated: # 로그인이 된 유저면
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        
            if user_profile.region_certification == 'Y':
                return render(request, 'carrot_app/write.html')
            else:
                return redirect('alert', alert_message='동네인증이 필요합니다.')
        except UserProfile.DoesNotExist:
            return redirect('alert', alert_message='동네인증이 필요합니다.')
    
    else: # 로그인이 되지 않은 유저면 
        return redirect('alert', alert_message = '로그인이 필요합니다.')