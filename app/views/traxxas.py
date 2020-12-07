from django.shortcuts import render, redirect

from app.forms.traxxas import TraxxasForm


def create_traxxas(request):
    if request.method == 'GET':
        context = {
            'form': TraxxasForm(),
        }
        return render(request, 'create.html', context)
    else:
        form = TraxxasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'create.html', context)


# def edit_recipe(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     if request.method == 'GET':
#         context = {
#             'recipe': recipe,
#             'form': RecipeForm(instance=recipe),
#         }
#         return render(request, 'edit.html', context)
#     else:
#         form = RecipeForm(request.POST, instance=recipe)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         context = {
#             'recipe': recipe,
#             'form': form,
#         }
#         return render(request, 'create.html', context)
#
#
# def delete_recipe(request, pk):
#     recipe = Recipe.objects.get(pk=pk)
#     if request.method == 'GET':
#         context = {
#             'recipe': recipe,
#             'form': DeleteRecipeForm(instance=recipe),
#         }
#         return render(request, 'delete.html', context)
#     else:
#         recipe.delete()
#         return redirect('index')
#
#
# def details_recipe(request, pk):
#     if Recipe.objects.exists():
#         recipe = Recipe.objects.get(pk=pk)
#         # ingredients_list = Recipe.ingredients
#         # ingredients_list.split(', ')
#         # recipe.ingredients_list = ingredients_list
#         context = {
#             'recipe': recipe,
#         }
#         return render(request, 'details.html', context)
#
