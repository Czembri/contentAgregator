-- DROP TRIGGER last_post_updated ON public.user_post;

create trigger last_post_updated before
update
    on
    public.user_post for each row execute function log_last_post_updated();