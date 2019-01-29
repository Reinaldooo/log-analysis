create view pathHits as
select path, count(*) as hits from log
where log.status = '200 OK' AND
path like '%article%'
group by path
order by hits desc;

