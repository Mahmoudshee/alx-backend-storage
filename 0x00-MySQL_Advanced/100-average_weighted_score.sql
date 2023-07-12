-- Create stored procedure ComputeAverageWeightedScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE avg_score FLOAT;

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

    UPDATE users SET average_score = avg_score WHERE id = user_id;
END //
DELIMITER ;

