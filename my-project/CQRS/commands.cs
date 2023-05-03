// Command model for adding a new dental procedure
class AddDentalProcedureCommand {
  constructor(public locationId: string, public procedureName: string, public procedureCost: number) {}
}

// Command handler for adding a new dental procedure
class AddDentalProcedureCommandHandler {
  constructor(private readonly dentalProcedureRepository: DentalProcedureRepository) {}

  async execute(command: AddDentalProcedureCommand): Promise<void> {
    const dentalProcedure = new DentalProcedure(command.procedureName, command.procedureCost);
    await this.dentalProcedureRepository.addDentalProcedure(command.locationId, dentalProcedure);
  }
}

// Query model for getting all dental procedures for a location
class GetDentalProceduresQuery {
  constructor(public locationId: string) {}
}

// Query handler for getting all dental procedures for a location
class GetDentalProceduresQueryHandler {
  constructor(private readonly dentalProcedureRepository: DentalProcedureRepository) {}

  async execute(query: GetDentalProceduresQuery): Promise<DentalProcedure[]> {
    return this.dentalProcedureRepository.getDentalProcedures(query.locationId);
  }
}

// Repository for managing dental procedures for each location
class DentalProcedureRepository {
  private readonly dentalProceduresByLocationId: Record<string, DentalProcedure[]> = {};

  async addDentalProcedure(locationId: string, dentalProcedure: DentalProcedure): Promise<void> {
    if (!this.dentalProceduresByLocationId[locationId]) {
      this.dentalProceduresByLocationId[locationId] = [];
    }
    this.dentalProceduresByLocationId[locationId].push(dentalProcedure);
  }

  async getDentalProcedures(locationId: string): Promise<DentalProcedure[]> {
    return this.dentalProceduresByLocationId[locationId] || [];
  }
}

// Dental procedure model
class DentalProcedure {
  constructor(public readonly name: string, public readonly cost: number) {}
}
