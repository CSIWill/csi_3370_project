-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema predatory_elephants
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema predatory_elephants
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `predatory_elephants` DEFAULT CHARACTER SET utf8 ;
USE `predatory_elephants` ;

-- -----------------------------------------------------
-- Table `predatory_elephants`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `predatory_elephants`.`customer` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `customer_fname` VARCHAR(45) NULL,
  `customer_lname` VARCHAR(45) NULL,
  `customer_gender` VARCHAR(45) NULL,
  `customer_phone` VARCHAR(45) NULL,
  `customer_address` VARCHAR(45) NULL,
  `weight` INT NULL,
  `height` INT NULL,
  `age` INT NULL,
  `customer_email` VARCHAR(45) NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE INDEX `customer_id_UNIQUE` (`customer_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `predatory_elephants`.`trainer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `predatory_elephants`.`trainer` (
  `trainer_id` INT NOT NULL AUTO_INCREMENT,
  `trainer_fname` VARCHAR(45) NULL,
  `trainer_lname` VARCHAR(45) NULL,
  PRIMARY KEY (`trainer_id`),
  UNIQUE INDEX `trainer_id_UNIQUE` (`trainer_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `predatory_elephants`.`routine`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `predatory_elephants`.`routine` (
  `routine_id` INT NOT NULL AUTO_INCREMENT,
  `routine_name` VARCHAR(45) NULL,
  `routine_date` DATETIME NULL,
  `routine_description` VARCHAR(45) NULL,
  `customer_customer_id` INT NOT NULL,
  `trainer_trainer_id` INT NOT NULL,
  INDEX `fk_routine_customer1_idx` (`customer_customer_id` ASC) VISIBLE,
  INDEX `fk_routine_trainer1_idx` (`trainer_trainer_id` ASC) VISIBLE,
  PRIMARY KEY (`routine_id`),
  UNIQUE INDEX `routine_id_UNIQUE` (`routine_id` ASC) VISIBLE,
  CONSTRAINT `fk_routine_customer1`
    FOREIGN KEY (`customer_customer_id`)
    REFERENCES `predatory_elephants`.`customer` (`customer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_routine_trainer1`
    FOREIGN KEY (`trainer_trainer_id`)
    REFERENCES `predatory_elephants`.`trainer` (`trainer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `predatory_elephants`.`workout`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `predatory_elephants`.`workout` (
  `workout_id` INT NOT NULL AUTO_INCREMENT,
  `sets` VARCHAR(45) NULL,
  `reps` VARCHAR(45) NULL,
  PRIMARY KEY (`workout_id`),
  UNIQUE INDEX `workout_id_UNIQUE` (`workout_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `predatory_elephants`.`routine_has_workout`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `predatory_elephants`.`routine_has_workout` (
  `routine_routine_id` INT NOT NULL,
  `workout_workout_id` INT NOT NULL,
  PRIMARY KEY (`routine_routine_id`, `workout_workout_id`),
  INDEX `fk_routine_has_workout_workout1_idx` (`workout_workout_id` ASC) VISIBLE,
  INDEX `fk_routine_has_workout_routine1_idx` (`routine_routine_id` ASC) VISIBLE,
  CONSTRAINT `fk_routine_has_workout_routine1`
    FOREIGN KEY (`routine_routine_id`)
    REFERENCES `predatory_elephants`.`routine` (`routine_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_routine_has_workout_workout1`
    FOREIGN KEY (`workout_workout_id`)
    REFERENCES `predatory_elephants`.`workout` (`workout_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

