import do2.functions.ethereal_cards
import mcfunction


if __name__ == '__main__':
    import sys
    mcfunction.save(skip="--skip" in sys.argv)