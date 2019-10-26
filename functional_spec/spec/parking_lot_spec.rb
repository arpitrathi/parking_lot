require 'spec_helper'

RSpec.describe 'Parking Lot' do
  let(:pty) { PTY.spawn('parking_lot') }

  before(:each) do
    run_command(pty, "create_parking_lot 3\n")
  end

  it "can create a parking lot", :sample => true do
    expect(fetch_stdout(pty)).to end_with("Created a parking lot with 3 slots\n")
  end

  it "can park a car" do
    run_command(pty, "park KA-01-HH-3141 Black\n")
    expect(fetch_stdout(pty)).to end_with("Allocated slot number: 1\n")
  end
  
  it "can unpark a car" do
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "leave 1\n")
    expect(fetch_stdout(pty)).to end_with("Slot number 1 is free\n")
  end
  
  it "can report status" do
    run_command(pty, "park KA-01-HH-1234 White\n")
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "park KA-01-HH-9999 White\n")
    run_command(pty, "status\n")
    expect(fetch_stdout(pty)).to end_with(<<-EOTXT
Slot No.    Registration No    Colour
1           KA-01-HH-1234      White
2           KA-01-HH-3141      Black
3           KA-01-HH-9999      White
EOTXT
)
  end

  it "can get slot number for given registration number" do
    run_command(pty, "park KA-01-HH-1234 White\n")
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "slot_number_for_registration_number KA-01-HH-1234\n")
    expect(fetch_stdout(pty)).to end_with("1\n")
   end

  it "can get license number for given car color" do
    run_command(pty, "park KA-01-HH-1234 White\n")
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "park KA-01-HH-9999 White\n")
    run_command(pty, "registration_numbers_for_cars_with_colour White\n")
    expect(fetch_stdout(pty)).to end_with("KA-01-HH-1234, KA-01-HH-9999\n")
  end

  it "can get slot number for given car color" do
    run_command(pty, "park KA-01-HH-1234 White\n")
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "park KA-01-HH-9999 White\n")
    run_command(pty, "slot_numbers_for_cars_with_colour White\n")
    expect(fetch_stdout(pty)).to end_with("1, 3\n")
  end

  it "can not found slot number for given registration number" do
    run_command(pty, "park KA-01-HH-1234 White\n")
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "park KA-01-HH-9999 White\n")
    run_command(pty, "slot_number_for_registration_number MH-01-HH-2134\n")
    expect(fetch_stdout(pty)).to end_with("Not found\n")
  end

  it "can not park extra car if all other slots are full" do
    run_command(pty, "park KA-01-HH-1234 White\n")
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "park KA-01-HH-9999 White\n")
    run_command(pty, "park MH-10-AB-7136 Red\n")
    expect(fetch_stdout(pty)).to end_with("Sorry, parking lot is full\n")
  end

  it "can show no cars sparked on getting status initially" do
    run_command(pty, "status\n")
    expect(fetch_stdout(pty)).to end_with("No cars present in the parking lot\n")
  end

  it "can show no cars parked after cars left the slot" do
    run_command(pty, "park KA-01-HH-1234 White\n")
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "leave 1\n")
    run_command(pty, "leave 2\n")
    run_command(pty, "status\n")
    expect(fetch_stdout(pty)).to end_with("No cars present in the parking lot\n")
  end

  it "can handle input for non existent slot numbers for given car color in the parking lot" do
    run_command(pty, "park KA-01-HH-1234 White\n")
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "park KA-01-HH-9999 White\n")
    run_command(pty, "slot_numbers_for_cars_with_colour Red\n")
    expect(fetch_stdout(pty)).to end_with("No cars found in the parking lot with colour Red\n")
  end

  it "can handle input for non existent registration number for given car color in the parking lot" do
    run_command(pty, "park KA-01-HH-1234 White\n")
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "park KA-01-HH-9999 White\n")
    run_command(pty, "registration_numbers_for_cars_with_colour Red\n")
    expect(fetch_stdout(pty)).to end_with("No cars found in the parking lot with colour Red\n")
  end

  it "can handle invalid commands as well" do
    run_command(pty, "invalid command\n")
    expect(fetch_stdout(pty)).to end_with("Please input valid commands\n")
  end
end
