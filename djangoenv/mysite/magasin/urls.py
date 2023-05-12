from django.urls import path,include
from . import views
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
urlpatterns =[
    path('',views.index,name='index'),
    path('affichefou/',views.affichefou,name='affichefou'),

    path('edit_product/',views.edit_product,name='edit_product'),
    path('list/edit/<int:product_id>/', views.edit_product, name='edit_product'),

    #path('produit_detail/',views.produit_detail,name='produit_detail'),

    path('view_product/',views.view_product,name='view_product'),
    path('list/<int:product_id>/view', views.view_product, name='view_product'),

    path('delete_product/',views.delete_product,name='delete_product'),
    path('list/<int:product_id>/Delete', views.delete_product, name='delete_product'),

    path('nouveauFournisseur/',views.nouveauFournisseur,name='nouveauFournisseur'),
    path('AddProd/',views.AddProd,name='AddProd'),
    
    path('register/',views.register, name = 'register'), 

    path('view_fournisseur/',views.view_fournisseur,name='view_fournisseur'),
    path('fou/<int:fou_id>/view', views.view_fournisseur, name='view_fournisseur'),

    path('edit_fournisseur/',views.edit_fournisseur,name='edit_fournisseur'),
    path('fou/edit/<int:fou_id>/', views.edit_fournisseur, name='edit_fournisseur'),

    path('delete_fou/',views.delete_fou,name='delete_fou'),
    path('fou/<int:fou_id>/Delete', views.delete_fou, name='delete_fou'),
    ####### Password rest #######
    path('password-reset/', PasswordResetView.as_view(template_name='magasin/users/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='magasin/users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='magasin/users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='magasin/users/password_reset_complete.html'),name='password_reset_complete'), 

    path('password-reset/', PasswordResetView.as_view(template_name='magasin/users/password_reset.html',html_email_template_name='users/password_reset_email.html'),name='password-reset'),
    

    path("add_commande",views.add_commande,name="Commande"),
    path('detail_commande/<int:id>/',views.commande_detail,name="detailcomm"),
 ]