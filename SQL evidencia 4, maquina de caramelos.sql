CREATE TABLE usuarios (id INT PRIMARY KEY,nombre VARCHAR(50),email VARCHAR(100));
CREATE TABLE ingredientes(saborizante_limon INT,saborizante_naranja INT, agua int, azucar int, colorante_anaranjado int,colorante_amarillo int)

alter table usuarios add column pedido_caramelos_naranja int
alter table usuarios add column pedido_caramelos_limon int

insert into usuarios(id, nombre,email,pedido_caramelos_naranja,pedido_caramelos_limon) values (123,'juan','juan@mail.com',1500,2000)
insert into usuarios(id, nombre,email,pedido_caramelos_naranja,pedido_caramelos_limon) values (456,'manuel','manu@mail.com',750,1100),(159,'jose','jose96@mail.com',2300,1800),(741,'ana','ana2024@mail.com',3250,2710)
insert into usuarios(id, nombre,email,pedido_caramelos_naranja,pedido_caramelos_limon) values (562,'miguel','mig@mail.com',0,1900),(98,'hernan','hernan@mail.com',980,0),(05,'lucia','luci89@mail.com',500,300)

select id from usuarios
select sum(pedido_caramelos_limon)from usuarios
select sum(pedido_caramelos_naranja)from usuarios
select azucar from ingredientes
select email from usuarios
