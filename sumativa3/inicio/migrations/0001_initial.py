from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_marca', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=50)),
                ('descripcion_producto', models.CharField(max_length=200)),
                ('valor_producto', models.IntegerField()),
                ('stock_producto', models.IntegerField()),
                ('imagen_producto', models.ImageField(upload_to='imagenes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categoria_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.categoria')),
                ('marca_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id rol de usuario')),
                ('nombre_rol', models.CharField(max_length=10, verbose_name='nombre rol de usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_producto',
            fields=[
                ('id_tipo_producto', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_tipo_producto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('total', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('correo_usuario', models.CharField(max_length=50)),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('pass_usuario', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rol_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.rol')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.proveedor'),
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.tipo_producto'),
        ),
        migrations.CreateModel(
            name='Detalle_venta',
            fields=[
                ('id_detalle', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.usuario')),
                ('ventas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.venta')),
            ],
        ),
    ]
