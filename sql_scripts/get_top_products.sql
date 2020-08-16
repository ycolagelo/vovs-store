
select p.name, pi.url
from product p
join product_image pi on p.id = pi.product_id
group by p.id, p.name
having pi.priority = min(pi.priority)
