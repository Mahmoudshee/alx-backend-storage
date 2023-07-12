-- Create stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE avg_score FLOAT;

    -- Declare cursor for selecting user IDs
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open cursor
    OPEN cur;

    -- Loop through each user
    read_loop: LOOP
        -- Fetch user ID from cursor
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate average weighted score
        SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO total_score, total_weight
        FROM corrections c
        INNER JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        IF total_weight IS NULL OR total_weight = 0 THEN
            SET avg_score = 0;
        ELSE
            SET avg_score = total_score / total_weight;
        END IF;

        -- Update user's average score
        UPDATE users SET average_score = avg_score WHERE id = user_id;
    END LOOP;

    -- Close cursor
    CLOSE cur;
END //
DELIMITER ;

