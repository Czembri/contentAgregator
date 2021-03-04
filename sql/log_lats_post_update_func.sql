CREATE OR REPLACE FUNCTION public.log_last_post_updated()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
declare
	user_id integer;
	action_name text;
BEGIN
	IF new.title <> OLD.title or new.content <> old.title 
	then
	user_id := (select pc.user_id from post_cooperators pc where pc.post_id = old.post_id);
	action_name := (select a.action_name from actions a where a.id = 1);
		INSERT INTO user_actions(user_id, action_name , changed_on, action_id)
			 VALUES(user_id, action_name, now(), 1);
	END IF;

	RETURN NEW;
END;
$function$
;
